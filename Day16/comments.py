# Define the Comment class below:
class Comment:
    def __init__(self, username, text, likes = 0):
        self.username = username
        self.text = text
        self.likes = likes

c = Comment("davey123", "lol you're so silly", 3) 
print(c. username)       #"davey123"
print(c. text)           #"lol you're so silly"
print(c.likes)           #3
another_comment = Comment("rosa77", "soooo cute!!!") 