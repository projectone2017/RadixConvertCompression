# -*- coding: utf-8 -*-
import sys
import Compress


def main(argc, argv):
    plain = "fa682034cce445cee0bc5f41c60c1841"  # sample data
    print("元データ({0:4d}):{1}".format(len(plain), plain))

    compress = Compress.Compress()
    compressed = compress.compress(plain)
    print("圧縮　　({0:4d}):{1}".format(len(compressed), compressed))
    uncompressed = compress.uncompress(compressed)
    print("解凍　　({0:4d}):{1}".format(len(uncompressed), uncompressed))
    return


if(__name__ == "__main__"):
    main(len(sys.argv), sys.argv)
    sys.exit()
