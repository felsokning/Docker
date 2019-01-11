#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Returns the current week number of the year.

As some countries (e.g.: Sweden) use week numbers for organisation, it's
important to be able to return the given week number in an easily referenced
code-base. This creates a webpage on port 80 to do just that.

TO RUN:
	python3 app.py

NOTE:
	As these strings are unicode strings, we must use python3, as any version before this
        treats all strings as ASCII. (Silly Americans, thinking everyone only uses ASCII...)

ATTRIBUTIONS/CREDITS:
	Original idea found on http://vecka.nu
"""

__author__ = "felsokning"
__copyright__ = "Copyright 2018"
__license__ = "MIT"

from flask import Flask
from uuid import getnode as get_mac
import datetime
import os
import random
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    quotes = list()
    quotes.append(u"Att skriva bra och att tala bra är bara fåfänga om man inte lever bra - heliga Birgitta")
    quotes.append(u"När allt det som var byggnaden har rivits ner och forslats bort finns alltid rummet kvar,"
                  "fyllt av solstrålar. - Lars Norén")
    quotes.append(u"Vänskap behöver inga ord. Den är ensamheten befriad från ensamhetens ångest."
                  " - Dag Hammarskjöld")
    # Because index starts at zero, need to remove one from length, so we don't index on null.
    random_int = random.randint(0, quotes.__len__() - 1)
    html = '<body bgcolor="#2d5fa1"><center><img src="/static/giphy34.gif" /></center>' \
           '<font color="#ffca20" size="32"><center>Veckan Nummer: {week}</center></font>' \
           '<font color="#ffca20" size="4"><center><i>{text}</i></center></font></body>'
    week_number = datetime.date.today().isocalendar()[1]
    return html.format(week=week_number, text=quotes[random_int])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

