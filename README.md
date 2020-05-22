# TextTeaser

=============

* TextTeaser borrowed from [here](https://github.com/IndigoResearch/textteaser)
* [One piece of literature](https://iopscience.iop.org/article/10.1088/1757-899X/190/1/012048/pdf)

## Installation

    >>> git clone git@github.com:Sticksword/textteaser-microservice.git
    >>> pip install -r requirements.txt

## How to Use

    >>> from textteaser import TextTeaser
    >>> tt = TextTeaser()
    >>> tt.summarize(title, text)

You can also test TextTeaser by running `python test.py`.

## virtualenv setup

`python3 -m venv my-new-venv`
`source my-new-venv/bin/activate`
`pip install -r requirements.txt` -> `pip` in the `venv` points to `pip3`
`python stuff.py` -> `python` in the `venv` also points to `python3`

## kube setup

`kubectl apply -f kubernetes/deployment.yml`

## good tutorials

* [flask on kubernetes](https://testdriven.io/blog/running-flask-on-kubernetes/)

### dependencies

* [newspaper3k](https://newspaper.readthedocs.io/en/latest/)

### improvements & todo

* [could add textrank algo into the mix with sentence similarity matrix using TfidfVectorizer](https://github.com/foprel/smmry/blob/master/app.py)

### resources

in addition to the textrank similarity matrix approach described above in improvements section, we could also research these and try to add the benefits:

* [some short story datasets for both extractice and abstractive approaches](https://github.com/m-chanakya/shortstories)
* [another example of similarity matrices in action](https://github.com/RebeccaMerrett/Papyrus--simple-but-effective-text-summarization-tool)
* [another example of i believe similarity matrices but manually done instead of using a library function like sklearn.feature_extraction.text.CountVectorizer and sklearn.feature_extraction.text.TfidfTransformer](https://github.com/andersonpaac/smmry-alternate)

* [deploying a keras dl model using flask and docker](https://medium.com/analytics-vidhya/deploy-your-first-deep-learning-model-on-kubernetes-with-python-keras-flask-and-docker-575dc07d9e76)
  * [related official keras tutorial](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html)

#### sites

* [awesome text summarization](https://github.com/icoxfog417/awesome-text-summarization)
* [overview of the state of the art for text summarization](https://www.sciencedirect.com/science/article/abs/pii/S0957417418307735)
  * [but this is a shorter more to the point medium article](https://medium.com/luisfredgs/automatic-text-summarization-with-machine-learning-an-overview-68ded5717a25)
* [a modern dl approach using pointer generator networks](https://github.com/abisee/pointer-generator)
  * encoders, decoders, LSTMs, attention mechanism
