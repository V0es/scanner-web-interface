from website import app
from website.backend.backend import get_scanner_list




from flask import render_template, request

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():

    
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        scanner_list = get_scanner_list()
        return render_template('index.html', dpis=[150, 200, 300])
    return render_template('index.html')