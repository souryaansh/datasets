import numpy as np
from flask import Flask, flash, redirect, render_template, request, session, abort
import pickle

hey = Flask(__name__)
@hey.route('/hello/')
def hello():
    return render_template('index1.html')
if __name__ == '__main__':
    hey.run( debug=True)
