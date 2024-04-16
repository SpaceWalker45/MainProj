from flask import Flask
import subprocess
import threading
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    foobar = __import__("iris-video-sceenshot.py")
    return "scn thanne"

@app.route("/image")
def image():
    global process
    process = subprocess.Popen(['python', "iris-position copy.py"])
    # def kill_process():
    #     if process.poll() is None:  # Check if the process is still running
    #         process.terminate()
    # timer = threading.Timer(10, kill_process)
    # timer.start()

    # # Wait for the process to finish
    # process.wait()

    # # Cancel the timer if the process finishes before the timeout
    # timer.cancel()
    return "scn thanne"

if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)  # Set d