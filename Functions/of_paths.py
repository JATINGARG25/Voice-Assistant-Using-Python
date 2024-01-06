# Offline function paths

import os
import subprocess as sp

paths = {
    'notepad': "C:\\Windows\\system32\\notepad.exe",
    'wordpad': "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe",
    'vs code': "C:\\Users\\gargj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    'command prompt': "C:\\Windows\\system32\\cmd.exe",
    'paint': "C:\\Windows\\system32\\mspaint.exe",
}

def open_notepad():
    os.startfile(paths['notepad'])

def open_wordpad():
    os.startfile(paths['wordpad'])

def open_vscode():
    os.startfile(paths['vs code'])

def open_cmd():
    os.startfile(paths['command prompt'])

def open_paint():
    os.startfile(paths['paint'])

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
