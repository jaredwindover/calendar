from math import ceil
from layout.utilities import (transpose,
                              groups,
                              rightPad)
from layout.block import Block
from layout.column import Column
from layout.coloredText import ColoredText

class Row(Block):
    def __init__(
            self,
            blocks,
            height=None,
            alignment="top",
            padding=0,
            color=None):
        self.blocks = blocks
        self._height = height
        self.alignment = alignment
        self.padding = padding
        self.color = color

    def wrap(self, count, columnize=False, columnProps={}):
        if (columnize):
            return Row(
                [
                    Column(rs, **columnProps)
                    for rs in transpose(groups(count, self.blocks))
                ],
                height=self._height,
                alignment=self.alignment,
                padding=self.padding,
                color=self.color
            )
        else:
            return Column([
                Row(
                    cs,
                    height=self._height,
                    alignment=self.alignment,
                    padding=self.padding,
                    color=self.color
                )
                for cs in groups(count, self.blocks)
            ], **columnProps)

    def render(self):
        rowHeight = self.height()
        results = [ColoredText("", self.color) for i in range(rowHeight)]
        widthSoFar = 0

        for block in self.blocks:
            widthSoFar += self.padding
            blockHeight = block.height()
            blockWidth = block.width()
            skip = 0
            if self.alignment == "bottom":
                skip = rowHeight - blockHeight
            elif self.alignment == "center":
                skip = ceil((rowHeight - blockHeight) / 2)
            renderedBlock = block.render()
            for i in range(blockHeight):
                results[i + skip].tokens.append(renderedBlock[i])
            widthSoFar += blockWidth
            for i in range(len(results)):
                results[i] = rightPad(results[i], widthSoFar)

        return results

    def height(self):
        if self._height is None:
            return max([block.height() for block in self.blocks])
        return self._height

    def width(self):
        numBlocks = len(self.blocks)
        return (sum([block.width() for block in self.blocks]) +
                self.padding * (numBlocks - 1))
