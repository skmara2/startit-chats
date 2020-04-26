import os
from flask import Flask, render_template, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config['SQLALCHEMY_DATABSE_URL'] = os.environ['DATABSE_URL']
db=SQLAlchemy(app)

class test(db.Model):
  col=db.Column(db.String(255), primary_key=True)
  col=db.Column(db.String(255), unique=True, nullable=False)
  
  def __repr__(self):
    return '%r' % self.col

@app.route('/')
def index_page():
  return render_template('chats.html')

@app.route('/health')
def health_check():
  return "OK" 

@app.route('/chats/lasi')
def ielasit_chatu():
  chata_rindas=[]
  with open("chats.txt", "r", encoding="UTF-8") as f:
    for rinda in f:
      chata_rindas.append(rinda)
  return jsonify({"chats":chata_rindas})  

@app.route('/chats/suuti', methods=['POST'])  
def suuti_zinu():
  dati=request.json
  with open("chats.txt", "a", newline="", encoding="UTF-8")as f:
     f.write(dati["chats"]+"\n")
  return ielasit_chatu()
    
@app.route('/postgreSQL')
def postgresSQL():
  result=test.query.all()
  return '%r' % result


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)
