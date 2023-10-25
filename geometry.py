import math


class HollowRing:
    """
    """

    def __init__(self, diameter, oteeth, iteeth):

        self.width = diameter
        self.height = diameter

        self.radius = diameter / 2
        self.center = (self.radius, self.radius)

        self.outer_teeth = oteeth
        self.inner_teeth = iteeth

        self.holes = []


class SolidDisc:
    """
    """

    def __init__(self, diameter, teeth):

        self.width = diameter
        self.height = diameter

        self.radius = diameter / 2
        self.center = (self.radius, self.radius)

        self.teeth = teeth

        self.holes = []


    def from_center(self, hole_num):

        return math.sqrt(abs((self.center[0] - self.holes[hole_num][0])) ** 2 + abs((self.center[1] - self.holes[hole_num][1])) ** 2)


class Ring144(HollowRing):

    def __init__(self):

        super().__init__(2248, 144, 96)

        self.holes = [
                (1380, 140),
                (1827, 409),
                (2073, 862),
                (2062, 1370),
                (1806, 1798),
                (1378, 2032),
                (893, 2021),
                (486, 1771),
                (262, 1360),
                (271, 903),
                (506, 510),
                (900, 303),
                (1331, 317),
                (1700, 540),
                ]

class Ring150(HollowRing):

    def __init__(self):

        super().__init__(2344, 150, 105)

        self.holes = [
                (950, 135),
                (1398, 144),
                (1783, 330),
                (2061, 656),
                (2172, 1063),
                (2115, 1473),
                (1900, 1816),
                (1562, 2040),
                (1170, 2106),
                (793, 2008),
                (494, 1770),
                (315, 1438),
                (289, 1066),
                ]


class Disc24(SolidDisc):

    def __init__(self):

        super().__init__(426, 24)

        self.holes = [
                (315, 249),
                (227, 302),
                (157, 258),
                (168, 174),
                (244, 177),
                ]


class Disc30(SolidDisc):

    def __init__(self):

        super().__init__(514, 30)

        self.holes = [
                (370, 145),
                (397, 231),
                (369, 309),
                (284, 353),
                (206, 324),
                (186, 245),
                (249, 193),
                (308, 244),
                ]


class Disc32(SolidDisc):

    def __init__(self):

        super().__init__(546, 32)

        self.holes = [
                (406, 169),
                (432, 257),
                (400, 333),
                (310, 385),
                (230, 363),
                (191, 277),
                (237, 210),
                (313, 219),
                (322, 292),
                ]


class Disc40(SolidDisc):

    def __init__(self):

        super().__init__(666, 40)

        self.holes = [
                (518, 197),
                (548, 296),
                (517, 417),
                (452, 478),
                (367, 502),
                (275, 475),
                (218, 403),
                (229, 287),
                (301, 241),
                (289, 266),
                (413, 348),
                (350, 397),
                (294, 339),
                ]


