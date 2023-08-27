import subprocess


def install_packages_from_requirements(requirements_file):
    try:
        subprocess.check_call(["pip", "install", "-r", requirements_file])
        print("Packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print("An error occurred while installing packages:", e)


if __name__ == "__main__":
    install_packages_from_requirements("requirements.txt")
