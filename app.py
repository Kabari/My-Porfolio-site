from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def index_2():
    return render_template('index-2.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# @app.route('/blog')
# def blog():
#     return render_template('blog.html')


if __name__ == '__main__':
    app.run(debug=True)