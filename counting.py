import re
import os
import zipfile
import string
import sys
from nltk.stem import PorterStemmer
from collections import Counter

with open('testlist.txt') as f:
    lines = f.readlines()
testingwords = lines[2].split()
lines[2] = "\t".join(testingwords) + "\n"
with open('testlist.txt', 'w') as file:
    file.writelines( lines )
print(lines[2])