from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/dados', methods=['POST'])
def form():
    dado_text = request.form.get('text-area')
    dado_radio = request.form.get('radio')
    return  render_template("form.html", text = dado_text, radio = dado_radio )
if __name__ == '__main__':
    app.run(debug=True)

