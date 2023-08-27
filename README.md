# Website :- Follow below steps to run this project
# Git and Python Install
git --version \
choco install gh \
refreshenv :- for refreshing the environment variable \
C:\Program Files\Git\bin :- add the path to git.exe in your PATH environment variable \
where anaconda \
C:\Users\ankit\anaconda3 :- add the path to python.exe in your PATH environment variable  \
python --version \
C:\Users\ankit\anaconda3\Scripts  :- add the path to pip.exe in your PATH environment variable \
pip --version \

# Git Command
gh auth login \
git clone https://github.com/ankitgupta24101/Website.git \
git remote -v \
git init \
git status \
git add filename \
git config --global user.email "email_id" \
git config --global push.autoSetupRemote true
git commit -m "First Commit" \
git push -u origin \
git pull origin \
git fetch \
git stash \
git switch main \

# Python Command
pip install -r requirements.txt \
pip install Django==4.2.4 \
python -m django --version \
django-admin startproject MyWebsite \
cd MyWebsite \
python manage.py startapp first_app \
python manage.py runserver \
python manage.py migrate \
python manage.py sqlmigrate first_app 0001 \
python manage.py makemigrations first_app \
python manage.py createsuperuser \