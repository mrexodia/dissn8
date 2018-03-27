# Simple script to extract the ROM data from a compiled SN8 file.
# Author: mrexodia

import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "usage: extractRom input.sn8 output.rom"
        sys.exit(1)

    in_file = open(sys.argv[1], "rb") # opening for [r]eading as [b]inary
    data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
    in_file.close()

    sn8_size = 24832
    if len(data) < sn8_size:
        print "ERROR: input file too small"
        sys.exit(1)

    if len(data) != 24832:
        print "WARNING: input file bigger than expected"

    out_file = open(sys.argv[2], "wb") # open for [w]riting as [b]inary
    out_file.write(data[256:][:(0x3000*2)])
    out_file.close()
    print "done!"