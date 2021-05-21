import string
import sys
import getopt
import pickle
import re
from nltk.stem import PorterStemmer
import os
import zipfile
from collections import Counter
from os import path
st = PorterStemmer()

def main(argv):
   terms = ''
   docs = ''
   doc = 0
   term = 0

   opts = sys.argv
   if (len(opts) != 3):
       sys.exit("Usage:  py ./VSM.py <query-file> <results-file>\n\n")
   qfile = opts[1]
   rfile = opts[2]
   if (path.exists(qfile) == False):
       sys.exit("Inputed query-file does not exist")
   print("Query File:" + qfile + " :: Results File:" + rfile)

if __name__ == "__main__":
    main(sys.argv[1:])