from flask import Flask
# remember to import roles along with users
app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug = True)