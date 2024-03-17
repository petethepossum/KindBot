from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parse', methods=['POST'])
def parse_text():
    text = request.form['text']
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)