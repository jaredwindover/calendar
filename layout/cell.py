from layout.block import Block
from layout.coloredText import ColoredText

class Cell(Block):
    def __init__(self, contents, color=None):
        self.contents = ColoredText(str(contents), color)

    def render(self):
        return [self.contents]

    def height(self):
        return 1

    def width(self):
        return len(self.contents)
