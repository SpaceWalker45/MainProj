from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    foobar = __import__("iris-video-sceenshot.py")
    return "scn thanne"

if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)  # Set d