# CS172 - Assignment 1 (Tokenization)

## Team member 1 - Firstname Lastname
Team member 1 - Omar Ochoa

###### Provide a short explanation of your design
-I used Pytho
-The code might not look too optimized since this is one of my first times working with python
-I did the extra credit method, but due to time constraints and my slow computer, I had to decrease the amount of ap89 files pased into the code to 11 of the provided files.
-It could index all files properly, but on my computer it would take a significant amount of time.
(How to run)
The script is run with 'py ./read_index.py --term TERM --doc DOCNAME' for passing in both a document and a term, 
or a singular term/doc argument if only one is being passed in
All calls run the same way as is specified in the assignment info except that the 'py' needs to be added at the beggining of the command line.
Not sure if that is just because I run it on a windows pc, but that is the way I had to write the command.

(Details)
-Part 1 works as is intended. I added the tokenizing code that stemms, lowerscases, removes punctuation, and removes stopwords
to the parsing.py file that was provided, the parsing file is then called within the read_index.py file but only does anything if new
files are added to ap89_collection_small
-Part 3 works as intended as well.It is fully written in the read_index.py file. Provided the required input for a document name or a file name or both, it outputs the desired statements describing
the term/document. Since I did this in the extra credit method, it works by reading the created text filed from the part 2 extra credit rather than reading
it from memory.
-Part 2 also works as intended in the extra credit, it creates the files term_info.txt, docids.txt, termids.txt, 
and term index files(I decided to save the term index files as seperate files rather than a single one). The main issue that I have in this part
is that, since my computer is not fast, I had to lower the amount of files that were passed in so that I could be able to turn in the assignment on time.
I had to remove several files from the provided ap89_collection_small so right now the index is only made up of a few files instead of all of them.
The files that are indexed are 'ap890101', 'ap890102', 'ap890103', 'ap890104', 'ap890105', ap890106', 'ap890107', 
'ap890108', 'ap890109', 'ap890110', and 'ap890321'
The code does work completely as it should and indexes any files that are passed to it, but due to time constraints and my slow computer, I had to
limit the amount of files that would get passed in.

(Extra Credit)
-Included stemming using the nltk.stem library
-Saved index to txt files rather than save them to memories for the indexing section as the extra credit stated.
-I implemented the term_index.txt into several files rather than a singular index file.
These files are saved in the base directory.
-As stated in the description of the extra credit, term_info's second value is now the textfile name for the term instead of the offset.