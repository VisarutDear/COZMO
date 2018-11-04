from flask import Flask, render_template
import os
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

import qrcodegen

@app.route('/')
def result():
    qrcodegen.generate()
    return render_template('result.html')

@app.after_request
def add_header(response):
    response.cache_control.max_age = 1
    response.cache_control.public = True
    return response

if __name__ == '__main__':
   app.run(debug = True)
