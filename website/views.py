from website import app
import backend




from flask import render_template, request

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():

    
    if request.method == 'post':
        pass
    if request.method == 'get':
        pass

    return render_template('index.html')