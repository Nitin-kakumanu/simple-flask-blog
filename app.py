from flask import request, render_template, Flask, redirect, url_for
from datetime import datetime

app= Flask(__name__)

posts = []

@app.route('/')

def index():
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST', 'GET'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        post = {
            'title' : title,
            'content' : content,
            'author': author,
            'date' : date
        }

        posts.append(post)
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)