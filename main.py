# coding: utf-8
import sys
import os
import datetime
import itertools
import re

import codecs
from tqdm import tqdm
import collections
import numpy as np
import pandas as pd
from pulp import *

from flask import *
from werkzeug import secure_filename
from werkzeug.datastructures import TypeConversionDict


# appの設定
app = Flask(__name__)

if os.path.exists('./uploads'):
    pass
else:
    os.mkdir('./uploads')
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if os.path.exists('./downloads/'):
    pass
else:
    os.mkdir('./downloads/')
DOWNLOADS_FOLDER = './downloads'
app.config['DOWNLOADS_FOLDER'] = DOWNLOADS_FOLDER


# トップ画面
@app.route('/')
def form():
    return render_template('home.html')


# pythonのversion確認
@app.route('/hello')
def hello():
    return "hello, developer!!"

if __name__ == "__main__":
    app.run(debug=True)
