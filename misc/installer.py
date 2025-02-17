from requests import get
import os

def save_link_as_file(link, filepath, bytes=False):
    r = get(link)
    with open(filepath, f"w{'b' if bytes else ''}") as f:
        f.write(r.content if bytes else r.text)

linkbase = "https://raw.githubusercontent.com/Tycho10101/LaunchiCube/refs/heads/main/"
save_link_as_file(f"{linkbase}misc/installer_backend.py", "installer_backend.py")
from installer_backend import *
installer_backend.install()
os.remove("installer_backend.py")
os.remove("installer.py")
