#OS: source ./venv/bin/activate
#Windows venv\Scripts\activate
from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():

    return render_template("index.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=4000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
