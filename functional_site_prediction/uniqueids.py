#!/usr/bin/python

#=================================================#
# uniqueids.py					  #
#						  #
# Michael Ting					  #
# 24 April 2013					  #
#						  #
# Extracts IDs from a sequence ID file to ensure  #
# ID's are non-redundant for alignment viewing	  #
# in belvu					  #
#=================================================#


import sys
from optparse import OptionParser
import re
import string

def main():

        parser = OptionParser()
        parser.add_option("-i", "--in", dest="infile", help="input sequence IDs file")
        parser.add_option("-o", "--out", dest="outfile", help="output non-redundant IDs file")

        (options, args) = parser.parse_args()

        infile = options.infile
        outfile = options.outfile

        idfile = open(infile)
        newfile = open(outfile, 'w')

	id_dict = dict()

        for line in idfile:
                nextid = line.split()
		idnum = str(nextid[0])
                
		if idnum not in id_dict.keys():
	                id_dict[idnum] = True
                	newfile.write(idnum+"\n")

        idfile.close()
        newfile.close()

if __name__ == "__main__":
        main()


