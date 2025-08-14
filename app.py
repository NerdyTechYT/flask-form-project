from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    with open('submissions.txt', 'a') as f:
        f.write(f"Name: {name}, Email: {email}\n")

    return "Thank you! Your info was saved."

if __name__ == '__main__':
    app.run(debug=True)
