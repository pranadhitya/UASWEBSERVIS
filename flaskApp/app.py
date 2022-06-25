from flask import Flask, json, request
from flask.templating import render_template
# from flask_mysqldb import MySQL
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer



app = Flask(__name__)


english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'db_web'
# app.config['MYSQL_PASSWORD'] = 'password'
# app.config['MYSQL_DB'] = 'db_user'
# mysql = MySQL(app)
# print(mysql)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignup', methods=['GET','POST'])
def showSignup():
    # _name=request.form['inputName']
    # _email=request.form['inpurEmail']
    # _number=request.form['inpurNumber']
    # _address=request.form['inpurAddress']
    # _password=request.form['inpurPassword']
    return render_template('signup.html')

    # if _name and _email and _number and _address and _password:
    #     return json.dumps({'html':'<span>All fields good !!</span>'})
    # else:
    #     return json.dumps({'html':'<span>Enter the required field</span>'})

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/boot")
def home():
    return render_template("boot.html")
 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))
 

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5500,debug=False)