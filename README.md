# TextTeaser

=============

TextTeaser borrowed from [here](https://github.com/IndigoResearch/textteaser)

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