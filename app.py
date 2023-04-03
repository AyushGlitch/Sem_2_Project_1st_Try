from flask import Flask, render_template, request, jsonify, redirect
from database import signup_to_db, login_from_db, water_bill_db, elec_bill_db, gas_bill_db,broadband_bill_db, update_elec_last_bill_date, update_water_last_bill_date, update_gas_last_bill_date, update_broadband_last_bill_date
import random
from datetime import date, datetime

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
  
@app.route("/login/dashboard")
def dashboard():
  return render_template('dashboard.html')

@app.route("/login/elec")
def elec():
  return render_template('elec.html')

@app.route("/login/gas")
def gas():
  return render_template('gas.html')

@app.route("/login/broadband")
def broadband():
  return render_template('broadband.html')

# @app.route("/login/dth")
# def dth():
#   return render_template('dth.html')

# @app.route("/login/mobile")
# def mobile():
#   return render_template('mobile.html')

@app.route("/login/water")
def water():
  return render_template('water.html')


@app.route("/elec/first_time")
def elec_first_time():
  today=date.today()
  id=random.randrange(2000000,3000000)
  return render_template('elec_first_time.html',today=today,id=id)

@app.route("/gas/first_time")
def gas_first_time():
  today=date.today()
  id=random.randrange(3000000,4000000)
  return render_template('gas_first_time.html',today=today,id=id)

@app.route("/water/first_time")
def water_first_time():
  today=date.today()
  id=random.randrange(1000000,2000000)
  return render_template('water_first_time.html',today=today,id=id)

@app.route("/broadband/first_time")
def broadband_first_time():
  today=date.today()
  id=random.randrange(4000000,5000000)
  return render_template('broadband_first_time.html',today=today,id=id)

@app.route("/elec/re")
def elec_re():
  today=date.today()
  return render_template("elec_re.html", today=today)


@app.route("/gas/re")
def gas_re():
  today=date.today()
  return render_template("gas_re.html", today=today)

@app.route("/water/re")
def water_re():
  today=date.today()
  return render_template("water_re.html", today=today)

@app.route("/broadband/re")
def broadband_re():
  today=date.today()
  return render_template("broadband_re.html", today=today)

@app.route("/elec/bill", methods=['post'])
def elec_bill():
  data= request.form
  # return jsonify(data)
  db_data=elec_bill_db(data)
  
  units=random.randrange(90,170)
  price_per_unit=10.73
  bill=units * price_per_unit

  curr_date = db_data['curr_date'].strftime('%Y-%m-%d')
  last_bill_date = db_data['last_bill_date'].strftime('%Y-%m-%d')
  
  if (datetime.strptime(curr_date, "%Y-%m-%d")-datetime.strptime(last_bill_date, "%Y-%m-%d")).days >30:
    update_elec_last_bill_date(data)
    return render_template('pay_elec_bill.html',db_data=db_data,units=units, price_per_unit=price_per_unit , bill=bill)

  else: 
    return render_template("no_bill.html")



@app.route("/gas/bill", methods=['post'])
def gas_bill():
  data= request.form
  # return jsonify(data)
  db_data=gas_bill_db(data)
  
  units=random.randrange(20,37)
  price_per_unit=25
  bill=units * price_per_unit

  curr_date = db_data['curr_date'].strftime('%Y-%m-%d')
  last_bill_date = db_data['last_bill_date'].strftime('%Y-%m-%d')
  
  if (datetime.strptime(curr_date, "%Y-%m-%d")-datetime.strptime(last_bill_date, "%Y-%m-%d")).days >30:
    update_gas_last_bill_date(data)
    return render_template('pay_gas_bill.html',db_data=db_data,units=units, price_per_unit=price_per_unit , bill=bill)

  else: 
    return render_template("no_bill.html")




@app.route("/water/bill", methods=['post'])
def water_bill():
  data= request.form
  # return jsonify(data)
  db_data=water_bill_db(data)
  
  curr_date = db_data['curr_date'].strftime('%Y-%m-%d')
  last_bill_date = db_data['last_bill_date'].strftime('%Y-%m-%d')
  
  if (datetime.strptime(curr_date, "%Y-%m-%d")-datetime.strptime(last_bill_date, "%Y-%m-%d")).days >30:
    update_water_last_bill_date(data)
    return render_template('pay_water_bill.html',db_data=db_data)

  else: 
    return render_template("no_bill.html")



@app.route("/broadband/bill", methods=['post'])
def broadband_bill():
  data= request.form
  # return jsonify(data)
  db_data=broadband_bill_db(data)
  
  curr_date = db_data['curr_date'].strftime('%Y-%m-%d')
  last_bill_date = db_data['last_bill_date'].strftime('%Y-%m-%d')
  
  if (datetime.strptime(curr_date, "%Y-%m-%d")-datetime.strptime(last_bill_date, "%Y-%m-%d")).days >30:
    update_broadband_last_bill_date(data)
    return render_template('pay_broadband_bill.html',db_data=db_data)

  else: 
    return render_template("no_bill.html")



@app.route("/login/bill_paid")
def bill_paid():
  return render_template('bill_paid.html')
  

if __name__ =='__main__':
  app.run(host='0.0.0.0', debug=True)