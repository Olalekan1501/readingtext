# Read text from a file, and count the occurence of words in that text
# Example:
# count_words "The cake is done. It is a big cake!") "it":1}
# →→> { "cake":2, "big":1, "is":2, "the":1, "a":1,

from collections import Counter
def read_file_content (filename): 
  # [assignment] Add your code here
  text_file = open(filename, 'r')
  text= text_file.read()
  return text

def count_words():
  text = read_file_content("./story.txt")
# Convert text files to lower case for harmony
  text= text.lower()
  # split the text into list of words
  words= text.split()
  #Remove white spaces, exclamation mark, questions etc
  [word.strip('.,!;[]') for word in words]
  #Replace apostrophe's with white space
  [word.replace("s",") for word in words]

  #count the unique words
  cnt = Counter() 
  for word in words:
    cnt[word] =+1
  return cnt