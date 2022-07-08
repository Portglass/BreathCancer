from windows import MyWindow
from bddConnection import bddRequest

conn = None
cur = None

def launcher(name):
    window = MyWindow(2)
    window.mainloop()


if __name__ == '__main__':
    launcher('PyCharm')