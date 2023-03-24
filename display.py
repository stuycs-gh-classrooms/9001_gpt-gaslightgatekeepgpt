class GraphicsEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[(0, 0, 0) for j in range(self.width)] for i in range(self.height)]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def save_image(self, filename):
        with open(filename, 'w') as f:
            f.write(f'P3\n{self.width} {self.height}\n255\n')
            for row in self.pixels:
                for r, g, b in row:
                    f.write(f'{r} {g} {b} ')

    def draw_line(self, x0, y0, x1, y1, color):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x, y = x0, y0
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        if dx > dy:
            err = dx / 2.0
            while x != x1:
                self.set_pixel(x, y, color)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y1:
                self.set_pixel(x, y, color)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        self.set_pixel(x, y, color)

    def draw_rectangle(self, x, y, width, height, color):
        for i in range(x, x + width):
            self.set_pixel(i, y, color)
            self.set_pixel(i, y + height - 1, color)
        for i in range(y, y + height):
            self.set_pixel(x, i, color)
            self.set_pixel(x + width - 1, i, color)

    def draw_circle(self, x, y, radius, color):
        x0, y0 = radius, 0
        err = 0
        while x0 >= y0:
            self.set_pixel(x + x0, y + y0, color)
            self.set_pixel(x + y0, y + x0, color)
            self.set_pixel(x - y0, y + x0, color)
            self.set_pixel(x - x0, y + y0, color)
            self.set_pixel(x - x


