import os
import subprocess

# Install necessary packages
subprocess.run(["pkg", "update", "-y"])
subprocess.run(["pkg", "upgrade", "-y"])
subprocess.run(["pkg", "install", "python", "-y"])
subprocess.run(["pkg", "install", "git", "-y"])
subprocess.run(["pkg", "install", "qt5-qtwebkit", "-y"])

# Clone Hexa Browser repository
subprocess.run(["git", "clone", "https://github.com/Hexa08/Hexa-Browser"])

# Change to Hexa Browser directory
os.chdir("hexa-browser-repo")

# Install additional Python packages if needed
subprocess.run(["pip", "install", "pyqt5"])

# Run the Hexa Browser CLI
subprocess.run(["python", "hexa_browser_cli.py"])
