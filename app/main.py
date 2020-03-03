# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from textteaser import TextTeaser
from newspaper import Article

app = Flask(__name__)

@app.route('/summarize')
def hello():
  url = request.args.get('url', '')
  print(url)

  article = Article(url)
  article.download()
  article.parse()

  title = article.title
  print(title)
  text = article.text
  print(text)

  tt = TextTeaser()

  sentences = tt.summarize(title, text)

  for sentence in sentences:
    print(sentence)

  return jsonify(sentences)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
