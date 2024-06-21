import os

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [['' for y in range(self._y)] for x in range(self._x)]

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self):
        os.system('cls')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(''.join([col[y] if col[y] != '' else ' ' for col in self._canvas]))


class TerminalScribe:
    def __init__(self, canvas):
        self._canvas = canvas
        self.pos = [0,0]
        self.mark = '*'
        self.trail = '.'

    def draw(self, pos):
        self._canvas.setPos(self.pos, self.mark)
        self.pos = pos
        self._canvas.setPos(self.pos, self.trail)
        self._canvas.print()

    def drawSquare(self, size, pos):
        x, y = pos
        
        for i in range(size - 1):
            self.draw([x + i, y])

        for i in range(size):
            self.draw([x + size - 1, y + i])

        for i in range(size):
           self.draw([x + size - 1 - i, y + size - 1])

        for i in range(size-1):
            self.draw([x, y + size-1-i])
        

canvas = Canvas(20, 20)
scribe = TerminalScribe(canvas)

scribe.drawSquare(5, [5,3])