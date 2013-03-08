#!/usr/bin/python

#=============================================================================#
# hmmscoreparser.py   							      #
# Michael Ting        							      #
# 20 February 2013							      #
#									      #
# Extracts the gi accession from hmmsearch --domtblout tabular form	      #
#									      #
# To run from the command line, use:					      #
#									      #
# $ python hmmscoreparser.py -i INFILE -o OUTFILE			      #
#									      #
# INFILE - the score file from using hmmsearch --domtblout		      #
# OUTFILE - a text file with all sequence hit gi accessions on separate lines #
# 									      #
# To read help information from the command line, type:			      #
# 									      #
# $ python hmmscoreparser.py -h						      #
#=============================================================================#


import sys
from optparse import OptionParser
import re
import string

def main():

	parser = OptionParser()
	parser.add_option("-i", "--in", dest="infile", help="input hmmsearch score file")
	parser.add_option("-o", "--out", dest="outfile", help="name of output file")

	(options, args) = parser.parse_args()

	infile = options.infile
	outfile = options.outfile

	scorefile = open(infile)
	newfile = open(outfile, 'w')
	
	for line in scorefile:
		infolist = line.split()
		accession = infolist[0]
		if accession[0:2] != "gi":
			continue

		acslist = [str(s) for s in accession.split('|') if s.isdigit()]
		acsnum = acslist[0]

		newfile.write(acsnum+"\n")

	scorefile.close()
	newfile.close()
		

if __name__ == "__main__":
	main()
