from flask import Flask, render_template
from PIL import Image
import socket
import pyautogui as pg
import qrcode


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("naver.com", 443))

web_qr = qrcode.make(f"http://{sock.getsockname()[0]}:5004")
web_qr.save("pointer_qr.png")

image = Image.open("pointer_qr.png")
image.show()


app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("pointer.html")

@app.route("/left", methods=['GET'])
def left_click():
    pg.press('left')
    return render_template("pointer.html")

@app.route("/right", methods=['GET'])
def right_click():
    pg.press('right')
    return render_template("pointer.html")

# if __name__ == 'main__':
app.run(host="0.0.0.0", port=5004, debug=False)
