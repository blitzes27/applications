import sys
import os
import base64
import socket
import webbrowser
import subprocess
from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

def select_folder():
    """Use osascript to pop up the native macOS folder chooser."""
    script = 'POSIX path of (choose folder with prompt "Choose a folder with images")'
    p = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True, text=True
    )
    if p.returncode != 0 or not p.stdout.strip():
        sys.exit("No folder chosen. Exiting.")
    return p.stdout.strip()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result")
def result():
    if not IMAGE_FOLDER:
        return (
            "No folder specified. "
            "Please relaunch the app by double-clicking the icon."
        ), 400

    images = []
    for fname in sorted(os.listdir(IMAGE_FOLDER)):
        if fname.lower().endswith((".png","jpg","jpeg","gif","bmp","webp")):
            path = os.path.join(IMAGE_FOLDER, fname)
            with open(path, "rb") as f:
                data = base64.b64encode(f.read()).decode("utf-8")
            images.append({
                "name": fname,
                "ext": fname.rsplit(".", 1)[1].lower(),
                "data": data,
            })
    return render_template("result.html", images=images)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        IMAGE_FOLDER = sys.argv[1]
    else:
        IMAGE_FOLDER = select_folder()

    # pick free port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", 0))
    port = sock.getsockname()[1]
    sock.close()

    webbrowser.open(f"http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, use_reloader=False)