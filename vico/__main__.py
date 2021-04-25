import argparse
import logging
import sys

import vico
import vico.context as ctx
import vico.ffmpeg as ff
from vico.gui import gui


logger = logging.getLogger("vico")


def parse(args):
    parser = argparse.ArgumentParser(description="Convert videos using ffmpeg")
    parser.add_argument(
        "--version", action="version", version="ViCo " + vico.__version__
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging"
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Disable all logging but errors"
    )
    parser.add_argument(
        "path",
        nargs="*",
        help="paths to videos to convert or directories containing videos to convert",
    )
    ctx.set_options(parser.parse_args(args))


def config_log():
    if ctx.get_option("quiet"):
        lvl = logging.ERROR
    elif ctx.get_option("verbose"):
        lvl = logging.DEBUG
    else:
        lvl = logging.INFO
    logging.basicConfig(
        format="%(asctime)s %(name)s %(levelname)s %(message)s", level=lvl
    )


def main(args):
    parse(args)
    config_log()

    ff.precheck()
    gui()


__name__ == "__main__" and main(sys.argv[1:])
