import subprocess
import sys
import os

# Define the path to your requirements.txt file
requirements_file = "requirements.txt"

# Check if the virtual environment exists
if not os.path.exists("venv"):
    # Create a new virtual environment
    subprocess.check_call([sys.executable, "-m", "venv", "venv"])

# Activate the virtual environment
if sys.platform == "win32":
    activate_script = os.path.join("venv", "Scripts", "activate.bat")
else:
    activate_script = os.path.join("venv", "bin", "activate")

subprocess.call([activate_script], shell=True)

# Install the packages listed in the requirements file
subprocess.check_call(["pip", "install", "-r", requirements_file])