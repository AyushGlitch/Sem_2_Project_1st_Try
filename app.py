from flask import Flask, render_template, request, jsonify, redirect
from database import signup_to_db, login_from_db, water_bill_db
import random
from datetime import date

app= Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/signup")
def signup():
  return render_template('signup.html')

@app.route("/signup/apply", methods=['post'])
def signup_done():
  data= request.form
  # return jsonify(data)
  signup_to_db(data)
  return render_template('signup_success.html')

@app.route("/login")
def login():
  return render_template('login.html')

@app.route("/login/success", methods=['post'])
def login_success():
  data= request.form
  is_user=login_from_db(data)

  if not is_user:
    return render_template('login_fail.html')

  return render_template('login_success.html')
  # return jsonify(data)
  

@app.route("/login/water")
def gas():
  return render_template('water.html')

@app.route("/water/first_time")
def gas_first_time():
  today=date.today()
  id=random.randrange(100000,200000)
  return render_template('water_first_time.html',today=today,id=id)

@app.route("/water/bill", methods=['post'])
def water_bill():
  data= request.form
  # return jsonify(data)
  db_data=water_bill_db(data)
  return render_template('pay_water_bill.html',db_data=db_data)

@app.route("/login/bill_paid")
def bill_paid():
  return render_template('bill_paid.html')
  

if __name__ =='__main__':
  app.run(host='0.0.0.0', debug=True)