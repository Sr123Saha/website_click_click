from flask import Flask, render_template

app = Flask(__name__)

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
