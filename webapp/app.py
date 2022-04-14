from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient("mongodb+srv://admin:admin@cluster0.riqct.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") #host uri
list_location = ['parking_db','parking_db_2','parking_db_3']

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@app.route('/redirect')
def options():
    option = request.args.get("location")
    return redirect(url_for('display',name = option))


@app.route('/display/<name>')
def display(name):
    id = name
    db = client.get_database(list_location[int(id)])
    records = db.parking_records
    questions = records.find()
    return render_template('about.html', posts=questions)

@app.route('/detail/<slot>/<name>', methods=['POST', 'GET'])
def detail(slot,name):
    parking_index = name
    slot_id = int(slot)
    if int(slot) < 20:
        row_id = 2
    db = client.get_database(list_location[int(parking_index)])
    records = db.parking_records
    questions = records.find_one({'order':slot_id})
    string_url = 'images/direction/{}/{}.png'.format(parking_index,row_id)
    return render_template('detail.html', posts=questions, string_url=string_url)



if __name__ == '__main__':
    app.run()
