import sys
import math

from PIL import Image, ImageDraw, ImageOps


class SpiroSim:
    """Spiral graphic simulation

       Two circular shapes create roulette curves, two of which are described here.

       When a circle rotates on the outside of another circle, the equations that govern
       pen position are called Epitrochoids.

       R = fixed.radius
       r = rotor.radius
       d = rotor.from_center(pen_hole)
       theta = 360 / fixed.outer_teeth

       def x(theta):
           return ((fixed.radius + rotor.radius) * math.cos(theta)) - (rotor.from_center(pen_hole) * math.cos(((R+r)/r)*theta)

       def y(theta):
           return ((fixed.radius + rotor.radius) * math.sin(theta)) - (rotor.from_center(pen_hole) * math.sin(((R+r)/r)*theta)

       In the opposite scenario, where a circle is rotating on the inside of another,
       the equation used is a Hypotrochoid.
    """

    def __init__(self, fixed, rotor, pen_hole=0, iters=10, filename='test.png', background=(255,0,0), line_color=(0,0,0), line_width=5, scale=1.0, border=50):

        self.iters = iters
        self.pen_hole = pen_hole

        self.fixed = fixed
        self.rotor = rotor

        self.bg_color = tuple(background)
        self.line_color = tuple(line_color)
        self.line_width = line_width
        self.border = border
        self.scale = scale

        self.fn = filename

        self.points = []


    def epitrochoid_x(self, R, r, d, theta):

        return ((R + r) * math.cos(theta)) - (d * math.cos(((R + r) / r) * theta))


    def epitrochoid_y(self, R, r, d, theta):

        return ((R + r) * math.sin(theta)) - (d * math.sin(((R + r) / r) * theta))


    def run(self):

        R = self.fixed.radius
        r = self.rotor.radius
        d = self.rotor.from_center(self.pen_hole)

        theta = 0.0
        angle_incr = 1.0 / ((2.0 * math.pi) ** 2)

        for i in range(self.iters):

            x, y = self.step(R, r, d, theta)
            self.points.append((x,y))

            theta += angle_incr


    def step(self, R, r, d, theta):

        x = self.epitrochoid_x(R, r, d, theta)
        y = self.epitrochoid_y(R, r, d, theta)

        return x, y


    def write_image(self):

        minx, miny, maxx, maxy = 0, 0, 0, 0
        for x, y in self.points:
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y

        img_size = (
                int(abs(minx - maxx)) + (self.border * 2),
                int(abs(miny - maxy)) + (self.border * 2)
                )

        x_offset = img_size[0] / 2.0
        y_offset = img_size[1] / 2.0

        self.image = Image.new('RGB', img_size, self.bg_color)

        draw = ImageDraw.Draw(self.image)

        prev_x, prev_y = None, None

        for idx, coords in enumerate(self.points):

            x, y = coords

            if prev_x and prev_y:
                draw.line(
                        (
                            prev_x + x_offset, prev_y + y_offset,
                            x + x_offset, y + y_offset
                            ),
                        fill=self.line_color,
                        width=self.line_width,
                        )

            prev_x, prev_y = x, y

            if idx > 0 and x == self.points[0][0] and y == self.points[0][1]:
                print('Broken at', idx)
                break

        if self.scale != 1.0:
            ImageOps.scale(self.image, self.scale)

        self.image.save(self.fn, 'PNG')


