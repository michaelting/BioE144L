#!/usr/bin/python

#=================================================#
# uniqueids.py                                    #
#                                                 #
# Michael Ting                                    #
# 24 April 2013                                   #
#                                                 #
# Extracts IDs from a sequence ID file to ensure  #
# ID's are non-redundant for alignment viewing    #
# in belvu                                        #
#=================================================#


import sys
from optparse import OptionParser
import re
import string

def main():

        parser = OptionParser()
        parser.add_option("-i", "--in", dest="infile", help="input ConSurf grades file")
        parser.add_option("-o", "--out", dest="outfile", help="output best scores file")

        (options, args) = parser.parse_args()

        infile = options.infile
        outfile = options.outfile

        idfile = open(infile)
        newfile = open(outfile, 'w')

        linelist = []

        for line in idfile:
                nextline = line.split()

		position = nextline[0]
		seq = nextline[1]
		color = nextline[4]

		if color == '9':
			newfile.write(position+"\t"+seq+"\t"+color+"\n")

        idfile.close()
        newfile.close()

if __name__ == "__main__":
        main()


