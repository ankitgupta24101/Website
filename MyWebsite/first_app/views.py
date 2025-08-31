import importlib.util
import os
import sys
from io import StringIO

from django.http import HttpResponse, JsonResponse
from django.template import Template, Context
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve

from .models import Home

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# External AiModel folder
AI_MODEL_FILE = os.path.normpath(os.path.join(BASE_DIR, '../AIModel/Model/Kitty_model.py'))
# Map folder names to their actual paths
STATIC_FOLDERS = {
    'CSS': os.path.join(BASE_DIR, '../HtmlWebsite/CSS/'),
    'Image': os.path.join(BASE_DIR, '../HtmlWebsite/Image/'),
    'JavaScript': os.path.join(BASE_DIR, '../HtmlWebsite/JavaScript/'),
}

def serve_static(request, folder, path):
    if folder in STATIC_FOLDERS:
        return serve(request, path, document_root=STATIC_FOLDERS[folder])
    else:
        return HttpResponse("Not Found", status=404)

# Serve dynamic HTML files
def serve_html(request, html_file='index.html'):  # default to index.html
    # Automatically append .html if not present
    if not html_file.endswith('.html'):
        html_file += '.html'
    # Build absolute path
    html_path = os.path.join(BASE_DIR, '../HtmlWebsite/Html/', html_file)
    html_path = os.path.normpath(html_path)  # normalize path

    # Debug: print path
    print(f"Loading HTML file: {html_path}")

    # Check if file exists
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return HttpResponse(content)
    else:
        return HttpResponse(f"HTML file not found: {html_file}", status=404)


def ai_page(request, html_file='ai.html'):
    # Full path to AI HTML file
    ai_html_path = os.path.join(BASE_DIR, '../AiModel', html_file)
    ai_html_path = os.path.normpath(ai_html_path)

    if os.path.exists(ai_html_path):
        with open(ai_html_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

        # Use Django template engine to render template tags dynamically
        template = Template(template_content)
        context = Context({'request': request})
        rendered_content = template.render(context)

        return HttpResponse(rendered_content)
    else:
        return HttpResponse(f"AI HTML file not found: {html_file}", status=404)

# ===================== AI Command Input =====================
@csrf_exempt
def ai_input(request):
    if request.method != "POST":
        return JsonResponse({"status": "error", "message": "Invalid request method."})

    command = request.POST.get("command", "").strip()
    if not command:
        return JsonResponse({"status": "error", "message": "No command provided."})

    try:
        # Dynamically load external Kitty.py
        spec = importlib.util.spec_from_file_location("Kitty", AI_MODEL_FILE)
        Kitty = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(Kitty)

        # Create instance of Assistant
        assistant = Kitty.Assistant()
        # Capture stdout for command output
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        # Execute command from external Kitty.py
        assistant.execute_command(command)

        sys.stdout = old_stdout
        output = mystdout.getvalue().strip()
        message = output if output else f"Executed: {command}"

        return JsonResponse({"status": "success", "message": message})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

def members(request):
    return HttpResponse("Hello world!")

def home(request):
    mymembers = Home.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Home.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
