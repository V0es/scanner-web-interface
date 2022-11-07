from website import app
from website.backend.utils import get_scanner_list, start_scanning
from config import file_extensions

import logging


from flask import render_template, request

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():

    scanner_list = get_scanner_list()

    if request.method == 'POST':
        start_scanning(request.form, scanner_list)
        
    if request.method == 'GET':
        logging.debug('Get method caught')    
        return render_template('index.html', scanners=scanner_list, extensions=file_extensions)
    return render_template('index.html')