from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("<h1>Welcome to our website!</h1>")

@app.route('/greet/<name>')
def greet(name: int):
    return render_template_string(f"<h1>Hello, {name}!</h1>")

if __name__ == '__main__':
    app.run(debug=True)
   