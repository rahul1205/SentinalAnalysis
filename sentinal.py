# import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
# from nltk.corpus import names


def word_dict(words):
    return dict([(word, True) for word in words])


positive_vocab = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)']
negative_vocab = ['bad', 'terrible','useless', 'hate', ':(']
neutral_vocab = ['movie', 'the', 'sound', 'was', 'is', 'actors', 'did', 'know', 'words', 'not', 'hello']

positive_features = [(word_dict(pos), 'positive') for pos in positive_vocab]
negative_features = [(word_dict(neg), 'negative') for neg in negative_vocab]
neutral_features = [(word_dict(neu), 'neutral') for neu in neutral_vocab]
train_set = negative_features + positive_features + neutral_features

classifier = NaiveBayesClassifier.train(train_set)
# Predict
neg = 0
pos = 0
neu = 0
sentence = raw_input("Enter a String:")
sentence = sentence.lower()
words = sentence.split(' ')
for word in words:
    classResult = classifier.classify(word_dict(word))
    print classResult, word
    if classResult == 'negative':
        neg = neg + 1
    if classResult == 'positive':
        pos = pos + 1
    if classResult == 'neutral':
        neu = neu + 1

print('Positive: ' + str(float(pos) / len(words)))
print('Negative: ' + str(float(neg) / len(words)))
print('Neutral: ' + str(float(neu) / len(words)))
