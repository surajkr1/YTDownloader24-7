
from flask import Flask , render_template , request , send_file, url_for
import pytube
import logging
import sys
import os
from pytube import YouTube
app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def homefnc():
    if request.method == "POST":
        try:
            youtube_url = request.form["url1"]
            path = 'E://'
            local_download_path = YouTube(youtube_url).streams[1].download(path)
            fname = local_download_path
            return send_file(fname, as_attachment=True)
            return render_template("index.html", cont="Downloading")
        except:
            logging.exception("Failed download")
            return "Video download failed!"
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)