from layout.block import Block
from layout.coloredText import ColoredText

from layout.utilities import (leftPad,
                              rightPad,
                              centerPad)

class Column(Block):

    def __init__(
            self,
            blocks,
            width=None,
            alignment="right",
            padding=0,
            color=None
    ):
        self.blocks = blocks
        self._width = width
        self.alignment = alignment
        self.padding = padding
        self.color = color

    def render(self):
        width = self.width()
        f = leftPad
        if (self.alignment == "left"):
            f = rightPad
        elif (self.alignment == "center"):
            f = centerPad
        results = []
        for block in self.blocks:
            for s in block.render():
                results.append(ColoredText(f(s, width), self.color))
            results += [ColoredText("") for i in range(self.padding)]
        if self.padding > 0:
            results = results[:-self.padding]
        return results

    def height(self):
        numBlocks = len(self.blocks)
        return (sum([block.height() for block in self.blocks]) +
                (numBlocks - 1) * self.padding)

    def width(self):
        if self._width is None:
            return max([block.width() for block in self.blocks])
        return self._width
