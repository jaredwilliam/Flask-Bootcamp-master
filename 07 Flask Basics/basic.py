from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Puppy!</h1>"

@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return 'This is a page for {}'.format(name)

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1] == 'y':
        return name[:-1] + 'iful'
    else:
        return name + 'y'

if __name__ == '__main__':
    app.run(debug=True)
