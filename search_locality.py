from __future__ import print_function  # Python 2/3 compatibility
from itertools import islice
import logging
import argparse
import re
import string
import os


__author__      = "Stephen Goncher"
__copyright__   = "Copyright 2017, Stelligent Systems, LLC"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_args():
	parser = argparse.ArgumentParser(description='Searches for terms within N context amount for text files in a directory')
	parser.add_argument('term1', help='first term to search for (phrases must be double quoted)')
	parser.add_argument('term2', help='second term to search for (phrases must be double quoted)')
	parser.add_argument('context', type=int, help='size of context N, where N is the number of words between the terms')
	parser.add_argument('dir', nargs='?', default='.', help='directory to read plain text files from, defaults to current directory')
	parser.add_argument('-t', '--test', help='executes unit, functional, and acceptance tests')

	args = parser.parse_args()
	dirName = args.dir
	term1 = args.term1
	term2 = args.term2
	context = args.context
	return term1, term2, context, dirName

def parse_files():
	for file in os.listdir(dirName):
		if file.endswith(".txt"):
			text = open(dirName+"/"+file, "r").read()
			termList = [word.strip(string.punctuation) for word in text.split()]
			find_terms(termList, file)

def find_terms(termList, file):
	termIter = iter(termList)
	for term in termIter:
		if term == term1:
			checkTerm = next(islice(termIter, context, context+1), '')
			if checkTerm == term2:
				print ("Found in file: " + file)
				break


term1, term2, context, dirName = get_args()
parse_files()