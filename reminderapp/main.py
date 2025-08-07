import time
import subprocess

while True:
    subprocess.run([
        "osascript","-e",
        'display notification "have a break sir" with title "take a break sir"'
    ])
    time.sleep(3600)

"""
    It runs the osascript command, which is the macOS command-line tool to execute AppleScript.
    -e means “execute the following AppleScript code
"""

"""
display notification is a native AppleScript command that shows a macOS notification.
"have a break sir" is the main message text.
with title "take a break" is the title of the notification.
"""