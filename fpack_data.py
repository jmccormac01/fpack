
#########################################################
#                                                       #
#                  fpack_data.py v1.0                   #
#                                                       #
#                     James McCormac                    #
#                                                       #
#########################################################
#
#   A recursive python script to go through and fpack 
#	all the data in a directory. FITS Files which are
# 	gzipped are unzipped, then fpacked. Normal FITS files
#	are fpacked directly and other files are left as they are
#
#
#   Revision History:	
#   v1.0   08/04/14 - script writen - JMCC
#

import os, os.path
import argparse as ap


parser=ap.ArgumentParser()
parser.add_argument("--n", help="runs the script in SIMULATION mode, no images are changed", action="store_true")
args=parser.parse_args()

# if DRYRUN > 0, no files are changed

if args.n:
	DRYRUN = 1
if not args.n:
	DRYRUN = 0

def GoIn(place):	
	os.chdir(place)
	h=os.getcwd()
	print h
	t=os.listdir('.')
	GetSummary(t)	
	for i in range(0,len(t)):
		if os.path.isdir(t[i]) == True:
			print "%s is a directory..." % (t[i])
			GoIn(t[i])
	os.chdir('../')
	return 0


def GetSummary(t):
	for i in range(0,len(t)):
		if ".fit" in t[i] and t[i].endswith(".gz"):
			print "\tZippedFit(s): %s..." % (t[i])
			print "\t\tUnzipping %s --> fpacking %s..." % (t[i],t[i].split('.gz')[0])
			if DRYRUN == 0:
				os.system('gunzip %s' % t[i])
				os.system('fpack -Y -D %s' % t[i].split('.gz')[0])
		if ".fts" in t[i] and t[i].endswith(".gz"):
			print "\tZippedFts: %s..." % (t[i])
			print "\t\tUnzipping %s --> fpacking %s..." % (t[i],t[i].split('.gz')[0])
			if DRYRUN == 0:
				os.system('gunzip %s' % t[i])
				os.system('fpack -Y -D %s' % t[i].split('.gz')[0])
		if ".fit" in t[i] and t[i].endswith(".fz"):
			print "\tFpackedFit(s): %s..." % (t[i])
			print "\t\tFile %s is fine, not touching..." % (t[i])
			continue
		if ".fts" in t[i] and t[i].endswith(".fz"):
			print "\tFpackedFit(s): %s..." % (t[i])
			print "\t\tFile %s is fine, not touching..." % (t[i])
			continue
		if ".fit" in t[i] and t[i].endswith(".gz") == False:
			print "\tFit(s): %s..." % (t[i])
			print "\t\tfpacking %s..." % (t[i])
			if DRYRUN == 0:
				os.system('fpack -Y -D %s' % t[i])
		if ".fts" in t[i] and t[i].endswith(".gz") == False:
			print "\tFts: %s..." % (t[i])
			print "\t\tfpacking %s..." % (t[i])	
			if DRYRUN == 0:
				os.system('fpack -Y -D %s' % t[i])
		if t[i].endswith(".gz") and ".fit" not in t[i] and ".fts" not in t[i]:
			print "\tZipped: %s..." % (t[i])
			print "\t\tFile %s is fine, not touching..." % (t[i])
	return 0


def main():
	here=os.getcwd()
	t=os.listdir(here)
	GetSummary(t)
	for i in range(0,len(t)):
		if os.path.isdir(t[i]) == True:
			print "%s is a directory..." % (t[i])
			GoIn(t[i])

if __name__ == '__main__':
	main()


