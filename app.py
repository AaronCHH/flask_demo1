from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html', name='home')

@app.route('/about')
def about():
  return render_template('about.html', name='about')

if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.jinja_env.auto_reload = True
  app.run(debug=True) 