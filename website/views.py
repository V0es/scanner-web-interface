from website import app
from website.backend.utils import get_scanner_list, start_scanning
from config import file_extensions, dpis

import logging


from flask import render_template, request

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():

    scanner_list = get_scanner_list()

    if request.method == 'POST':
        start_scanning(request.form, scanner_list)
        
          
    return render_template('index.html', scanners=scanner_list, extensions=file_extensions, dpis=dpis)