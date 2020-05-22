# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import nltk.data
import os


class Parser:
    def __init__(self):
        self.ideal = 20.0
        self.stopWords = self.getStopWords()

    def getKeywords(self, text):
        text = self.removePunctations(text)
        words = self.splitWords(text)
        words = self.removeStopWords(words)
        uniqueWords = list(set(words))

        keywords = [{'word': word, 'count': words.count(word)} for word in uniqueWords]
        keywords = sorted(keywords, key=lambda x: -x['count'])

        return (keywords, len(words))

    def getSentenceLengthScore(self, sentence):
        return (self.ideal - abs(self.ideal - len(sentence))) / self.ideal

    # Jagadeesh, J., Pingali, P., & Varma, V. (2005). Sentence Extraction Based Single Document Summarization. International Institute of Information Technology, Hyderabad, India, 5.
    def getSentencePositionScore(self, i, sentenceCount):
        normalized = i / (sentenceCount * 1.0)

        if normalized > 0 and normalized <= 0.1:
            return 0.17
        elif normalized > 0.1 and normalized <= 0.2:
            return 0.23
        elif normalized > 0.2 and normalized <= 0.3:
            return 0.14
        elif normalized > 0.3 and normalized <= 0.4:
            return 0.08
        elif normalized > 0.4 and normalized <= 0.5:
            return 0.05
        elif normalized > 0.5 and normalized <= 0.6:
            return 0.04
        elif normalized > 0.6 and normalized <= 0.7:
            return 0.06
        elif normalized > 0.7 and normalized <= 0.8:
            return 0.04
        elif normalized > 0.8 and normalized <= 0.9:
            return 0.04
        elif normalized > 0.9 and normalized <= 1.0:
            return 0.15
        else:
            return 0

    def getTitleScore(self, title, sentence):
        titleWords = self.removeStopWords(title)
        sentenceWords = self.removeStopWords(sentence)
        matchedWords = [word for word in sentenceWords if word in titleWords]

        return len(matchedWords) / (len(title) * 1.0)

    def splitSentences(self, text):
        tokenizer = nltk.data.load('file:' + os.path.dirname(os.path.abspath(__file__)) + '/trainer/english.pickle')

        return tokenizer.tokenize(text)

    def splitWords(self, sentence):
        return sentence.lower().split()

    '''
    could also try regex approach: https://github.com/xiaoxu193/PyTeaser/blob/master/pyteaser.py

    from re import split as regex_split, sub as regex_sub, UNICODE as REGEX_UNICODE
        def split_words(text):
            #split a string into array of words
            try:
                text = regex_sub(r'[^\w ]', '', text, flags=REGEX_UNICODE)  # strip special chars
                return [x.strip('.').lower() for x in text.split()]
            except TypeError:
                print "Error while splitting characters"
                return None
    '''
    def removePunctations(self, text):
        return ''.join(t for t in text if t.isalnum() or t == ' ')

    def removeStopWords(self, words):
        return [word for word in words if word not in self.stopWords]

    def getStopWords(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/trainer/stopWords.txt') as file:
            words = file.readlines()

        return [word.replace('\n', '') for word in words]
