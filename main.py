 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/tutors')
def tutors():
  return render_template('tutors.html')

@app.route('/lessons')
def lessons():
  return render_template('lessons.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

if __name__ == '__main__':
  app.run(debug=True)


 수정된 main.py 파일 코드는 다음과 같습니다.


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/tutors')
def tutors():
  return render_template('tutors.html')

@app.route('/lessons')
def lessons():
  return render_template('lessons.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

if __name__ == '__main__':
  app.run(debug=True)
