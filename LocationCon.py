import win32gui
from PIL import ImageGrab

def setLocation(x, y):
        hwnd = win32gui.FindWindow(None, "BMO")
        win32gui.MoveWindow(hwnd, x, y, 1080, 1080, True)
        bbox = win32gui.GetWindowRect(hwnd)
        bmg = ImageGrab.grab(bbox)