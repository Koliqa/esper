import flask
import os


app = flask.Flask(__name__)

@app.route('/yo_nigga')
def mofaker():
    return 'GO FUCK YOURSELF!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
