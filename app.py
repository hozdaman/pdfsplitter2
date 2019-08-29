from flask import *
import pdfsplitter

app = Flask(__name__)


@app.route("/")
def upload():
    return render_template("file_upload.html")

@app.route("/success", methods=["POST"])
def success():
    global file
    f = request.files['file']
    file = f.filename
    f.save(file)
    return render_template("success.html", name = file)

@app.route("/convert")
def splitter():
    pdfsplitter.splitter(file)
    return render_template("download.html")

@app.route("/download")
def download():
    filename = file.split(".")[0] + "split.pdf"
    return send_file(filename, as_attachment= True)

    

if __name__ == "__main__":
    app.run(debug=True)
