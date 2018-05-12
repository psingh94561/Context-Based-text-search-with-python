import unittest, threading
from Tkinter import *

class clickThread(threading.Thread):
    def __init__(self, root):
        threading.Thread.__init__(self)
        self.root = root

    def run(self):
        button = filter(lambda a: isinstance(a, Button), self.root.children.values())[0]
        print(button)
        button.focus()
        button.event_generate("<Button-1>")
        button.event_generate("<ButtonRelease-1>")
        print("clicked")

class Test(unittest.TestCase):
    def testName(self):
        root = Tk()
        button = Button(root, command=self.returnEvent)
        button.pack()
        thread = clickThread(root)
        thread.start()
        root.mainloop()

    def returnEvent(self):
        print ("!")