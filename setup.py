import os
import subprocess

if os.path.isfile("requirements.txt"):
    print("Installing dependencies...")
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
else:
    print("No requirements.txt file found.")