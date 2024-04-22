import warnings
warnings.filterwarnings("ignore")

from flask import Flask, render_template, request
from logic import logic_function

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve the text from the textarea
        text = request.form.get('textarea')
        logic_function(text)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
