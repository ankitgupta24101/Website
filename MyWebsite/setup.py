import subprocess
import sys
import os
from pathlib import Path
import pytesseract
from PIL import Image
import numpy as np
def install_packages_from_requirements(requirements_file):
    try:
        subprocess.check_call(["pip", "install", "-r", requirements_file])
        print("Packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print("An error occurred while installing packages:", e)


if __name__ == "__main__":
    print("PyCharm is using:", sys.executable)
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(BASE_DIR)
    print(np.__version__)
    print(np.__file__)
    print(np.ndarray)
    print(pytesseract.get_tesseract_version())
    install_packages_from_requirements("requirements.txt")
