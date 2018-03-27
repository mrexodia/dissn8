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

    if len(data) == sn8_size + 60: # firmware embedded in Lenovo's tp_compact_usb_kb_with_trackpoint_fw.exe
        data = data[:sn8_size]
    elif len(data) != sn8_size:
        print "ERROR: input file bigger than expected"
        sys.exit(1)

    data = data[256:] # strip the SN8 header
    
    flash_size = 0x3000 * 2
    if len(data) != flash_size:
        print "ERROR: incorrect flash size (this should never happen)"
        sys.exit(1)

    footer = data[-16:]
    if footer != "\x00\x00\x00\x00\x00\x00\x00\x00\xF4\xFF\x24\x79\x5A\xFA\x58\x45":
        print "ERROR: unexpected footer (%s)" % repr(footer)
        sys.exit(1)

    data = data[:flash_size - 16] # strip footer

    out_file = open(sys.argv[2], "wb") # open for [w]riting as [b]inary
    out_file.write(data)
    out_file.close()
    print "done!"