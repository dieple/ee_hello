# from time import sleep
#
# while True:
#     print("Hello World!!!")
#     sleep(1)
from flask import Flask
# from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!!!'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)