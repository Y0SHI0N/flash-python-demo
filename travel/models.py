from cgitb import text
from email.mime import image


class Destination:
    def __init__(self):
        self.name = None
        self.currency = None
        self.description = None
        self.image = None
        self.comment = []
    
    def addCommment(self, txt):
        self.comment.append(txt)

class Comment:
    def __init__(self):
        self.User = None
        self.text = None
        self.creat_at = None
