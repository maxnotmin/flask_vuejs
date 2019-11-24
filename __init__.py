from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    print("Hellow world")
    return "hello world"




if __name__ == '__main__':
    app.run()