from textblob import *


wiki = TextBlob("Python is a high-level, general-purpose programming language.")
wiki.tags
[('Python', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('high-level', 'JJ'), ('general-purpose', 'JJ'), ('programming', 'NN'), ('language', 'NN')]
wiki.noun_phrases
WordList(['python'])

testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
testimonial.sentiment
Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857)
testimonial.sentiment.polarity
0.39166666666666666