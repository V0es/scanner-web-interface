from website import app


from flask import render_template, request

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'post':
        pass



    return render_template('index.html')