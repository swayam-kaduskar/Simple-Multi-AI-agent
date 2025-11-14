from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get data from the form
    number = request.form.get('number')
    result = int(number) ** 2  # Example: square the number
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
