from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/QuiSommesNous')
def QuiSommesNous():
    return render_template('QuiSommesNous.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/lmao')
def lmao():
    return render_template('lmao.html')

if __name__=='__main__':
    app.run()
