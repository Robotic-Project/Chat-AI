import win32gui
from PIL import ImageGrab

# Open notepad.exe manually.
def setLocation(x, y):
    hwnd = win32gui.FindWindow(None, "WINDOW HANDLE")
    win32gui.MoveWindow(hwnd, x, y, 500, 500, True)
    bbox = win32gui.GetWindowRect(hwnd)
    bmg = ImageGrab.grab(bbox)