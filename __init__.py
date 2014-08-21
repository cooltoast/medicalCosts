from flask import Flask, request, Response, redirect, render_template, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQL_DATABASE_URI', 'sqlite:///costs.db')
db = SQLAlchemy(app)

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.route("/submit_procedure")
def submitProcedure():
  name = request.args.get('name', None)
  cost = request.args.get('cost', None)

  if name is None:
    raise InvalidUsage('must supply name', status_code=400) 
  if cost is None:
    raise InvalidUsage('must supply cost', status_code=400) 

  try:
    costInt = int(cost)
  except ValueError:
    raise InvalidUsage('cost must be a number', status_code=400)

  procedure = Procedure(name, costInt)
  db.session.add(procedure)
  db.session.commit()
  
  return redirect('/')


# TODO make a better intro page
@app.route("/")
def displayIndex():
  return render_template('index.html')

@app.route("/show_procedures")
def showProcedures():
  procedures = Procedure.query.all() 
  
  return render_template('procedures.html', procedures=procedures)

@app.errorhandler(InvalidUsage)
def handleInvalidUsage(error):
  response = jsonify(error.to_dict())
  response.status_code = error.status_code
  return response

class Procedure(db.Model):
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  cost = db.Column(db.Integer)


  def __init__(self, name, cost):
    self.name = name
    self.cost = cost

  def __repr__(self):
    return '<Procedure object %s>' % self.name

if __name__ == "__main__":
    debug = 'DEBUG' in os.environ.keys()
    app.run(port=4000, debug=debug)

