"""
This Py sheet will handle the logic of the program
"""
from textmanage import Notepad

np = Notepad()
np.read_file()

print("Executing Input-Loop")
while True:
    t = input()
    if t == "!": break
    if t == "~":
        np.remove(input("What do you want to remove? "))
        np.show_text()
        continue
    if t == "@@":
        np.show_text()
        continue
    np.buffer(t)
    np.show_text()
    print("Loop end reached")
np.write_to_file()