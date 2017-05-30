class Block:
    def __str__(self):
        rend = [str(line) for line in self.render()]
        return '\n'.join(rend)

    def render(self):
        pass

    def height(self):
        pass

    def width(self):
        pass
