import string
import sys

# number of positions to shift
SHIFT = 1

# Create the mapping table
mapping_table = string.printable.replace(string.whitespace, '') + "ÄÖÜäöüß "


def encode(clearText):
    encodedText = ""
    print("encode: Input=" + clearText)
    for e in clearText:
        encodedText = encodedText + mapping_table[(mapping_table.index(e) + SHIFT) % len(mapping_table)]
    print("encode: Output=" + encodedText)


def decode(encodedText):
    clearText = ""
    print("decode: Input=" + encodedText)
    for e in encodedText:
        clearText = clearText + mapping_table[(mapping_table.index(e) - SHIFT) % len(mapping_table)]
    print("decode: Output=" + clearText)


def main(argv):
    if len(argv) == 2 and argv[0] == "-e":
        encode(argv[1])
    elif len(argv) == 1:
        decode(argv[0])
    else:
        print("Usage: encode_decode [-e] <text>")
        exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
