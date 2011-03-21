#!/usr/bin/evn python
# encoding: utf-8

import sys
from optparse import OptionParser
import instayc

def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage)
    parser.add_option("-a", "--add", action="store", type="string",
        dest="add", help="add tags to your config", metavar="TAGS")

    (options, args) = parser.parse_args()

    if options.add:
        print "adding tags"
    if len(args) == 0:
        print "Grabbing urls"

if __name__ == '__main__':
    main()
