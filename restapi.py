import flask
from flask import request,render_template
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
@app.route('/download')
def downloadurl():
  url=request.args.get('url')
  return '''<h1>the url is:{}</h1>'''.format(url)
@app.route('/user/<name>')
def user(name):
  return render_template('user.html',name=name)
app.run()