#!/usr/bin/env python
# coding: utf-8


import os
import sys


SOURCE_START = 0x3C
CHARMAP = {
    "\x98": "┌",
    "\x95": "─",
    "\x99": "┐",
    "\x96": "│",
    "\x9B": "┘",
    "\x9A": "└",
}


def main():
    try:
        binary, source = sys.argv[1:3]
    except ValueError:
        print >>sys.stderr, "Petit Computer Binary to Source Converter\n\nUse:\n\n  ./binsrc.py RPRG000.PTC pong.bas\n"
        sys.exit(1)

    with open(binary, "rb") as binfile:
        binfile.seek(SOURCE_START)
        raw_code = binfile.read()

    code = raw_code.replace("\r", os.linesep)

    for src, target in CHARMAP.iteritems():
        code = code.replace(src, target)

    with open(source, "w") as srcfile:
        srcfile.write(code)


if __name__ == "__main__":
    main()

