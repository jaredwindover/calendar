clearColor = '\033[0m'

class ColoredText:
    def __init__(self, text, color=None):
        self.tokens = [text]
        self.color = color

    def __str__(self):
        text = ''.join([str(token) for token in self.tokens])
        if self.color is None:
            return text
        return self.color + text + clearColor

    def __len__(self):
        return sum([len(token) for token in self.tokens])
