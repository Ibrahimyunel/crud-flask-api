from flask_app import app

@app.route('/name/<string:myname>')
def name(myname):
    return 'my name is {}'.format(myname)