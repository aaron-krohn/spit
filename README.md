# SPiral Image Tool

A utility to create PNG files with simulations of rotating gears

In its current form, it uses mathematical formulae describing circles that rotate inside or outside of other circles. The technical name for these drawings are [Hypotrochoids](https://en.wikipedia.org/wiki/Hypotrochoid) and [Epitrochoids](https://en.wikipedia.org/wiki/Epitrochoid), respectively.

With circles, the math is pretty simple, so it's what is currently supported. Although simulating other types of shapes is considerably more difficult, it is something I would eventually like this library to support.

# Example

```
./spit.py \
    --rotor-shape Disc40 \
    --fixed-shape Ring150 \
    --circumscription outer \
    --output-file spiro.png \
    --bg-color 255 0 0 \
    --line-color 0 0 0 \
    --line-width 10 \
    --pen-hole 2 \
    --iterations 15000
```

![Disc 40, Ring 150, hole 2, 15k iterations](./spiro.png?raw=true)

# Usage

```
$ ./spit.py --help
usage: spit - SPiral Image Tool [-h] [-r {Disc40}] [-f {Ring150}] [-c {inner,outer}] [-p PEN_HOLE] [-o OUTPUT_FILE] [-i ITERATIONS] [-b BG_COLOR BG_COLOR BG_COLOR] [-l LINE_COLOR LINE_COLOR LINE_COLOR] [-w LINE_WIDTH]
                                [-s SCALING_FACTOR] [-x BORDER_SIZE]

Simulates a spiral drawing tool

options:
  -h, --help            show this help message and exit
  -r {Disc40}, --rotor-shape {Disc40}
                        The geometry class name for the rotating shape
  -f {Ring150}, --fixed-shape {Ring150}
                        The geometry class name for the fixed shape
  -c {inner,outer}, --circumscription {inner,outer}
                        Whether the rotor rolls around the inside or outside of the fixed shape. Only used for Rings.
  -p PEN_HOLE, --pen-hole PEN_HOLE
                        Hole number of the shape used for drawing
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        File location of the output image
  -i ITERATIONS, --iterations ITERATIONS
                        Number of simulation tests to run
  -b BG_COLOR BG_COLOR BG_COLOR, --bg-color BG_COLOR BG_COLOR BG_COLOR
                        Comma separated RGB integer color of background
  -l LINE_COLOR LINE_COLOR LINE_COLOR, --line-color LINE_COLOR LINE_COLOR LINE_COLOR
                        Color of line to draw
  -w LINE_WIDTH, --line-width LINE_WIDTH
                        Width of drawn line in pixels
  -s SCALING_FACTOR, --scale SCALING_FACTOR
                        Scaling factor for the image
  -x BORDER_SIZE, --border-pixels BORDER_SIZE
                        Number of pixels to border image
```
