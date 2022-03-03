
from flask import Flask , render_template , request , send_file, url_for
import pytube
import sys
import os
import glob
from pytube import YouTube
app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def homefnc():
    
    if request.method == "POST":
        youtube_url = request.form["url1"]
        for name in glob.glob('Videos/*.mp4', recursive = True):
            print(name)
            os.remove(name)
        path = "Videos"
        local_download_path = YouTube(youtube_url).streams[1].download(path)
        fname = local_download_path
        return send_file(fname, as_attachment=True)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
