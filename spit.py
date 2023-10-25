#!/usr/bin/env python3.11

import argparse

from simulate import SpiroSim
from geometry import Ring150, Ring144, Disc24, Disc40


def init_args():

    parser = argparse.ArgumentParser(
            prog='spit - SPiral Image Tool',
            description='Simulates a spiral drawing tool',
            epilog=''
            )

    parser.add_argument(
            '-r', '--rotor-shape',
            default='Disc40',
            choices=['Disc40'],
            required=False,
            dest='rotor_class',
            help='The geometry class name for the rotating shape',
            action='store'
            )
    parser.add_argument(
            '-f', '--fixed-shape',
            default='Ring150',
            choices=['Ring150', 'Ring144', 'Disc24'],
            required=False,
            dest='fixed_class',
            help='The geometry class name for the fixed shape',
            action='store'
            )
    parser.add_argument(
            '-c', '--circumscription',
            default='outer',
            choices=['inner','outer'],
            required=False,
            dest='circumscribes',
            help='Whether the rotor rolls around the inside or outside of the fixed shape. Only used for Rings.',
            action='store'
            )
    parser.add_argument(
            '-p', '--pen-hole',
            default=0,
            type=int,
            required=False,
            dest='pen_hole',
            help='Hole number of the shape used for drawing',
            action='store'
            )
    parser.add_argument(
            '-o', '--output-file',
            default='spiro.png',
            required=False,
            dest='output_file',
            help='File location of the output image',
            action='store'
            )
    parser.add_argument(
            '-i', '--iterations',
            default=1000,
            type=int,
            required=False,
            dest='iterations',
            help='Number of simulation tests to run',
            action='store'
            )
    parser.add_argument(
            '-b', '--bg-color',
            type=int,
            nargs=3,
            default=[255,255,255],
            required=False,
            dest='bg_color',
            help='Comma separated RGB integer color of background',
            action='store'
            )
    parser.add_argument(
            '-l', '--line-color',
            type=int,
            nargs=3,
            default=[0,0,0],
            help='Color of line to draw',
            required=False,
            dest='line_color',
            action='store'
            )
    parser.add_argument(
            '-w', '--line-width',
            type=int,
            default=5,
            help='Width of drawn line in pixels',
            required=False,
            dest='line_width',
            action='store'
            )
    parser.add_argument(
            '-s', '--scale',
            default=1.0,
            help='Scaling factor for the image',
            type=float,
            required=False,
            dest='scaling_factor',
            action='store'
            )
    parser.add_argument(
            '-x', '--border-pixels',
            default=50,
            type=int,
            help='Number of pixels to border image',
            required=False,
            dest='border_size',
            action='store'
            )

    args = parser.parse_args()
    return args

if __name__ == '__main__':

    conf = init_args()

    # Do this better
    if conf.fixed_class == 'Ring150':
        fixed = Ring150()
    elif conf.fixed_class == 'Disc24':
        fixed = Disc24()
    else:
        print('ERROR: invalid fixed geometry')

    # Do this better
    if conf.rotor_class == 'Disc40':
        rotor = Disc40()
    else:
        print('ERROR: invalid rotor geometry')

    sim = SpiroSim(
            fixed,
            rotor,
            pen_hole=conf.pen_hole,
            iters=conf.iterations,
            filename=conf.output_file,
            background=conf.bg_color,
            line_color=conf.line_color,
            line_width=conf.line_width,
            scale=conf.scaling_factor,
            border=conf.border_size
            )

    sim.run()

    sim.write_image()
