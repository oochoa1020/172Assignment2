import re
import os
import zipfile
import string
import sys
from nltk.stem import PorterStemmer
from collections import Counter
import pickle
from os import path
import re

st = PorterStemmer()
original_stdout = sys.stdout
filescount = 0
# Regular expressions to extract data from the corpus
doc_regex = re.compile("<DOC>.*?</DOC>", re.DOTALL)
docno_regex = re.compile("<DOCNO>.*?</DOCNO>")
text_regex = re.compile("<TEXT>.*?</TEXT>", re.DOTALL)


with zipfile.ZipFile("ap89_collection_small.zip", 'r') as zip_ref:
    zip_ref.extractall()
   
# Retrieve the names of all files to be indexed in folder ./ap89_collection_small of the current directory
for dir_path, dir_names, file_names in os.walk("ap89_collection_small"):
    allfiles = [os.path.join(dir_path, filename).replace("\\", "/") for filename in file_names if (filename != "readme" and filename != ".DS_Store")]

thisdict = {
    "termid": "termfile"
}
if path.exists("dictionary.pk"):
    with open('dictionary.pk', 'rb') as fi:
        thisdict = pickle.load(fi)
else:
    with open("dictionary.pk", 'a') as fi:
        pass
curcounts = {
    "numtimes": 0
}
if path.exists("curcounts.pk"):
    with open('curcounts.pk', 'rb') as fi:
        curcounts = pickle.load(fi)
else:
    with open("curcounts.pk", 'a') as fi:
        pass
for file in allfiles:
    countwords = 0
    with open('stopwords.txt') as f:
        stopwords=[word for line in f for word in line.split()]
    with open(file, 'r', encoding='ISO-8859-1') as f:
        filedata = f.read()
        result = re.findall(doc_regex, filedata)  # Match the <DOC> tags and fetch documents

        for document in result[0:]:
            # Retrieve contents of DOCNO tag
            docno = re.findall(docno_regex, document)[0].replace("<DOCNO>", "").replace("</DOCNO>", "").strip()
            # Retrieve contents of TEXT tag
            text = "".join(re.findall(text_regex, document))\
                      .replace("<TEXT>", "").replace("</TEXT>", "")\
                      .replace("\n", " ")
            newtext = text.translate(str.maketrans('', '', string.punctuation))
            # lower-case
            newtext = newtext.lower()
            # splits then stems and removes stopwords
            splitstring = newtext.split()
            words  = [st.stem(word) for word in splitstring if word not in stopwords]
            newtext = ' '.join(words)
            unique = list(set(words))
            # finds amount of total terms in the document
            doclength = len(words)
            curcounts[docno] = doclength
            # Doc Index
            with open('docids.txt', 'a') as file:
                this = "this"
            with open('docids.txt', 'r') as file:
                data = file.read()
            line_count = len(open("docids.txt").readlines())
            with open('docids.txt', 'a') as file:
                if docno not in data:
                    sys.stdout = file
                    docid= "doc".strip() + str(line_count).strip()
                    print("doc", line_count, "\t", docno,sep="")
                    line_count += 1
                    sys.stdout = original_stdout
                    ##occurs = [m.start() for m in re.finditer('wow', string)]
                    ##content.index('test')
                    ## Term Index
                    with open('term_info.txt', 'a') as infofile:
                        pass
                    with open('termids.txt', 'a') as afile:
                        this = "this"
                        with open('termids.txt', 'r') as afile:
                            data = afile.read().split()
                            line_count = len(open("termids.txt").readlines())
                            with open('termids.txt', 'a') as afile:
                                for i in range(len(unique)):
                                    if unique[i] not in data:
                                        sys.stdout = afile
                                        print(line_count, "\t", unique[i],sep="")
                                        sys.stdout = original_stdout
                                       # thisdict[unique[i]] = line_count
                                        newfile = str(line_count).strip() + ".txt".strip()
                                        thisdict[unique[i]] = newfile
                                        occurs = [m.start() for m in re.finditer(unique[i], newtext)]
                                        with open('term_info.txt', 'a') as infofile:
                                            totcount = len(occurs)
                                            totdoccount = 1
                                            sys.stdout = infofile
                                            print(line_count, "\t", newfile, "\t", totcount, "\t", totdoccount,sep="")
                                            sys.stdout = original_stdout
                                        with open(newfile, 'a') as innerfile:
                                            for j in range(len(occurs)):
                                                innerfile.write(docid + ":" + str(occurs[j]) + "\t")
                                        data.append(unique[i])
                                        line_count += 1
                                    elif unique[i] in data:
                                        with open('termids.txt') as myFile:
                                            for num, line in enumerate(myFile, 0):
                                                if unique[i] in line:
                                                    curline = num
                                    #    curnum = thisdict[unique[i]]
                                     #   newfile = str(curnum) + ".txt".strip()
                                        curfile = newfile = str(curline) + ".txt".strip()
                                        occurs = [m.start() for m in re.finditer(unique[i], newtext)]
                                     #   added = ""
                                        with open(curfile, 'a') as ainnerfile:
                                            for k in range(len(occurs)):
                                                ainnerfile.write(docid + ":" + str(occurs[k]) + "\t")
                                        with open('term_info.txt', 'r') as file:
                                            infolines = file.readlines()
                                        seplines = infolines[curline].split()
                                        with open('term_info.txt', 'w') as infofile:
                                            totcount = len(occurs)
                                            seplines[2] = str(int(seplines[2]) + totcount)
                                            totdoccount = 1
                                            seplines[3] = str(int(seplines[3]) + 1)
                                            infolines[curline] = "\t".join(seplines) + "\n"
                                            infofile.writelines( infolines )
            ##print("linecount = ", line_count)
    with open("dictionary.pk", 'wb') as fi:
        pickle.dump(thisdict, fi)
    with open("curcounts.pk", 'wb') as fi:
        pickle.dump(curcounts, fi)
            ##print(len(splitstring), " : ", doclength)
                
            
            # step 1 - lower-case words, remove punctuation, remove stop-words, etc. 
            # step 2 - create tokens 
            # step 3 - build index
            