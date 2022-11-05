from website import app
from website.backend.backend import get_scanner_list
from config import file_extensions

import logging


from flask import render_template, request

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():

    
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        logging.debug('Get method caught')
        scanner_list = get_scanner_list()
        return render_template('index.html', scanners=scanner_list, extensions=file_extensions)
    return render_template('index.html')