import datetime
import os
import sys
import time
import webbrowser
import queue
import shutil
import urllib.request
import zipfile

import pyautogui
import pyttsx3

# Optional voice recognition
try:
    import sounddevice as sd
    from vosk import Model, KaldiRecognizer
    VOICE_AVAILABLE = True
except ImportError:
    VOICE_AVAILABLE = False


class Assistant:
    def __init__(self, vosk_model_dir="vosk-model-small-en-us-0.15"):
        self.vosk_model_dir = vosk_model_dir
        self.voice_enabled = VOICE_AVAILABLE
        self.q = queue.Queue() if self.voice_enabled else None

        if self.voice_enabled:
            self._init_voice_model()

        # Map commands to functions
        self.commands_map = {
            "time": self.speak_time,
            "date": self.speak_date,
            "screenshot": self.take_screenshot,
            "open notepad": self.open_notepad,
            "hello": self.say_hello,
            "open youtube": self.open_youtube,
            "open spotify": self.open_spotify,
            "explode srs": self.fake_bomb,
            "edit videos": self.open_video_editor,
            "video editor": self.open_video_editor,
            "calculator": self.open_calculator,
            "paint": self.open_paint,
            "quit": self.exit_assistant,
            "exit": self.exit_assistant,
        }

    # ===================== Initialization =====================
    def _init_voice_model(self):
        """Initialize Vosk voice recognition model."""
        try:
            self.vosk_model_dir = self.ensure_vosk_model(self.vosk_model_dir)
            self.model = Model(self.vosk_model_dir)
            self.recognizer = KaldiRecognizer(self.model, 16000)
        except Exception as e:
            print(f"[ERROR] Voice model initialization failed: {e}")
            self.voice_enabled = False

    # ===================== Text-to-Speech =====================
    def speak(self, text: str):
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"[TTS Error]: {e}")

    def speak_time(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.speak(f"The time is {now}")

    def speak_date(self):
        today = datetime.date.today().strftime("%B %d, %Y")
        self.speak(f"Today's date is {today}")

    def say_hello(self):
        self.speak("Hello! How are you today?")

    # ===================== Utilities =====================
    def take_screenshot(self):
        filename = f"screenshot_{int(time.time())}.png"
        pyautogui.screenshot().save(filename)
        self.speak("Screenshot taken.")
        print(f"[INFO] Saved screenshot as {filename}")

    def open_program(self, program_name: str, display_name: str):
        try:
            os.system(program_name)
            self.speak(f"Opening {display_name}.")
        except Exception as e:
            print(f"[ERROR] {display_name}: {e}")
            self.speak(f"Could not open {display_name}.")

    def open_notepad(self):
        self.open_program("notepad.exe", "Notepad")

    def open_video_editor(self):
        self.open_program("start filmora.exe", "Video Editor")

    def open_calculator(self):
        self.open_program("calc.exe", "Calculator")

    def open_paint(self):
        self.open_program("mspaint.exe", "Paint")

    def open_youtube(self):
        self.speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    def open_spotify(self):
        self.speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com")

    def fake_bomb(self, countdown: int = 5):
        self.speak("Starting countdown")
        for i in range(countdown, 0, -1):
            print(f"💣 {i}")
            self.speak(str(i))
            time.sleep(1)
        self._show_explosion_animation()

    def _show_explosion_animation(self):
        os.system("cls" if os.name == "nt" else "clear")
        frames = [
            "      *      ",
            "   *  *  *   ",
            " *   💥   * ",
            "   *  *  *   ",
            "      *      ",
            "             ",
        ]
        for frame in frames:
            print(frame)
            time.sleep(0.5)
            os.system("cls" if os.name == "nt" else "clear")
        self.speak("Boom! Just kidding. No real bomb here.")

    def ensure_vosk_model(self, model_dir):
        """Download and extract Vosk model if missing."""
        if os.path.exists(model_dir) and os.path.isdir(model_dir) and os.path.exists(os.path.join(model_dir, "conf")):
            return model_dir

        print(f"[INFO] Downloading Vosk model to {model_dir} ...")
        url = "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
        zip_path = "vosk_model.zip"

        urllib.request.urlretrieve(url, zip_path)
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(".")
        os.remove(zip_path)

        if not os.path.exists(model_dir):
            for f in os.listdir("."):
                if f.startswith("vosk-model") and os.path.isdir(f):
                    shutil.move(f, model_dir)
                    break
        return model_dir

    # ===================== Voice Recognition =====================
    def _callback(self, indata, frames, time_, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def listen_forever(self):
        if not self.voice_enabled:
            print("[INFO] Voice recognition not available.")
            return

        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                               channels=1, callback=self._callback):
            print("[INFO] Voice control ready. Say something...")
            import json
            while True:
                data = self.q.get()
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    text = result.get("text", "")
                    if text:
                        print("[VOICE INPUT]:", text)
                        self.execute_command(text)

    # ===================== Command Handling =====================
    def execute_command(self, command: str):
        command = command.lower()
        for key, func in self.commands_map.items():
            if key in command:
                func()
                return
        self.speak("Sorry, I didn't understand that command.")

    def exit_assistant(self):
        self.speak("Goodbye! Shutting down.")
        sys.exit()

    # ===================== Main Loop =====================
    def run(self):
        print("Choose mode: ")
        print("1. Voice Command Mode")
        print("2. Typing Mode")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1" and self.voice_enabled:
            self.speak("Voice mode activated. I am listening...")
            self.listen_forever()
        elif choice == "2":
            self.speak("Typing mode activated. Please type your commands.")
            while True:
                try:
                    command = input(">> ").strip()
                    if command:
                        self.execute_command(command)
                except KeyboardInterrupt:
                    self.speak("Exiting typing mode.")
                    break
        else:
            print("[ERROR] Invalid choice or voice not available.")


if __name__ == "__main__":
    Assistant().run()
