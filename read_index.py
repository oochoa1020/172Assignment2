# This file should contain code to receive either a document-id or word or both and output the required metrics. See the assignment description for more detail.
import string
import sys
import getopt
import parsing
import pickle
import re
from nltk.stem import PorterStemmer
st = PorterStemmer()
# s = "This. @#$%^^#^^&&(thing) here."
## now = s.translate(str.maketrans('', '', string.punctuation))
# print(now)
def main(argv):
   terms = ''
   docs = ''
   doc = 0
   term = 0
   try:
      opts, args = getopt.getopt(argv,"",["term=","doc="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == "--doc":
         doc = 1
         docs = arg
      elif opt in ("--term"):
         term = 1
         terms = arg
   if (doc & term):
       print("Inverted list for term:", terms)
       print("In document:", docs)
       currentword = st.stem(terms)
       spaceword = '\t' + currentword + '\n'
       curterm = -1
       with open('termids.txt') as termidfile:
           for termnum, line in enumerate(termidfile, 0):
               if spaceword in line:
                   curterm = termnum
       if curterm == -1:
           print("Term not found")
       else:
           with open('termids.txt', 'r') as file:
               termlines = file.readlines()
           splitlines = termlines[curterm].split()
           termsid = splitlines[0]
           with open('term_info.txt', 'r') as file:
               terminfolines = file.readlines()
           infolines = terminfolines[curterm].split()
           termtotal = infolines[2]
           termtotdoc = infolines[3]
           termloc = infolines[1]
       curdoc = -1
       with open('docids.txt') as docidfile:
           for docnum, line in enumerate(docidfile, 0):
               if docs in line:
                   curdoc = docnum
       if (curdoc == -1) or (curterm == -1):
           print("Document or term not found")
       else:
           with open('curcounts.pk', 'rb') as fi:
               curcounts = pickle.load(fi)
           with open('docids.txt', 'r') as file:
               doclines = file.readlines()
           splitlines = doclines[curdoc].split()
           docid = splitlines[0]
           with open(termloc, 'r') as file:
               termdata = file.read()
           splitdata = termdata.split("\t")
           searchdoc = docid.strip() + ":".strip()
           counttimes = termdata.count(searchdoc)
           positions = []
           for i in range(len(splitdata)):
               if splitdata[i].find(searchdoc) != -1:
                   positionsplit = splitdata[i].split(":")
                   positions.append(positionsplit[1])
               else:
                   pass
           print("TERMID:", termsid)
           print("DOCID:", docid)
           print("Term frequency in document:", counttimes)
           if counttimes == 0:
               print("Positions: 0")
           else:
               jointpos = ", ".join(positions)
               print("Positions:", jointpos)

   elif (doc):
       print("Listing for document:", docs)
       curdoc = -1
       with open('docids.txt') as docidfile:
           for docnum, line in enumerate(docidfile, 0):
               if docs in line:
                   curdoc = docnum
       if curdoc == -1:
           print("Document not found")
       else:
           with open('curcounts.pk', 'rb') as fi:
               curcounts = pickle.load(fi)
           with open('docids.txt', 'r') as file:
               doclines = file.readlines()
           splitlines = doclines[curdoc].split()
           docid = splitlines[0]
           print("DOCID:", docid)
           print("Total terms:", curcounts[docs])
   elif (term):
       print("Listing for term:", terms)
       currentword = st.stem(terms)
       spaceword = '\t' + currentword + '\n'
       curterm = -1
       with open('termids.txt') as termidfile:
           for termnum, line in enumerate(termidfile, 0):
               if spaceword in line:
                   curterm = termnum
       if curterm == -1:
           print("Term not found")
       else:
           with open('termids.txt', 'r') as file:
               termlines = file.readlines()
           splitlines = termlines[curterm].split()
           termsid = splitlines[0]
           print("TERMID:", termsid)
           with open('term_info.txt', 'r') as file:
               terminfolines = file.readlines()
           infolines = terminfolines[curterm].split()
           termtotal = infolines[2]
           termtotdoc = infolines[3]
           print("Number of documents containing term:", termtotdoc)
           print("Term frequency in corpus:", termtotal)
       

if __name__ == "__main__":
    main(sys.argv[1:])