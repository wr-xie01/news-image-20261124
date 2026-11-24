#!/usr/bin/env python3
"""Entry point: copy the built image to the output directory.

Reads entry.png next to this file and writes it to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
Guards: the file must be a PNG of at most 1 MiB and at most
1024 by 1024 pixels. Deterministic: both runs write the same bytes.
"""
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
MAX_BYTES = 1048576
MAX_DIM = 1024


def png_size(path):
    with open(path, "rb") as fh:
        head = fh.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file")
    if head[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        raise ValueError("entry.png is %d bytes, over the 1 MiB limit" % size)
    width, height = png_size(SRC)
    if width > MAX_DIM or height > MAX_DIM:
        raise ValueError("entry.png is %dx%d, over the 1024x1024 limit"
                         % (width, height))
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    print("wrote %s (%d bytes, %dx%d)" % (dst, size, width, height))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        sys.exit(1)
