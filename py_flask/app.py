from flask import Flask,jsonify
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home_page():
    return 'Welcome To HomePage!'

if __name__ == "__main__":
    app.run(debug=True)
    app.run()
    try: 
        from controller import *
    except Exception as e:
            print(e)


