import sys
import nltk
nltk.download('punkt')

text = sys.argv[1]
sentences = nltk.tokenize.sent_tokenize(text)

print (sentences)