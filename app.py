from flask import Flask, render_template, jsonify, request

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
  return render_template('signup_success.html')

if __name__ =='__main__':
  app.run(host='0.0.0.0', debug=True)