from sqlalchemy import create_engine, text

db_conn_string= "mysql+pymysql://pddvisif24pz1ud9x9yz:pscale_pw_ma8rMIXJVylKuAFvT1Ez4SmBs9j7eTabsAuJKtBNqgg@aws.connect.psdb.cloud/project_ayush_part?charset=utf8mb4"

engine = create_engine(db_conn_string,
                      connect_args={
                        "ssl": {
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })

def signup_to_db(data):
  with engine.connect() as conn:
    query = text("INSERT INTO users (full_name, email, userid, pwd, phone, account_no, account_pwd) VALUES (:full_name, :email, :userid, :pwd, :phone, :account_no, :account_pwd)")

    conn.execute(query, { 
                 'full_name': data['full_name'],
                 'email':data['email'],
                 'userid':data['username'],
                 'pwd':data['pwd'],
                 'phone':data['phone'],
                 'account_no':data['account_no'],
                 'account_pwd':data['account_pwd']
    })

def login_from_db(data):
  with engine.connect() as conn:
    result = conn.execute(
          text("select * from users where userid=:id and pwd=:pwd"),
            {"id": data['username'],
             "pwd": data['pwd']}
    )
    rows = []
    rows=[dict(zip(result.keys(), row)) for row in result]
      
    if len(rows) == 0:
      return None
    else:
      return (rows[0])

def water_bill_db(data):
  with engine.connect() as conn:
    result = conn.execute(
          text("select * from water where phone=:phone"),
            {"phone": data['phone']}
    )
    rows = []
    rows=[dict(zip(result.keys(), row)) for row in result]
      
    if len(rows) == 0:
      with engine.connect() as conn:
        query = text("INSERT INTO water (id, phone, email, curr_date) VALUES (:id, :phone, :email, :curr_date)")

        conn.execute(query, { 
                 'id':data['id'],
                 'phone':data['phone'],
                 'email':data['email'],                 
                 'curr_date':data['today'],
                 
        })
        water_bill_db(data)
    
    else:
      conn.execute(
          text("update water set curr_date=:today where         phone=:phone"),
            {"today" : data['today'],
              "phone": data['phone']}
      )
      return (rows[0])


def update_water_last_bill_date(data):
  with engine.connect() as conn:
    conn.execute(
          text("update water set last_bill_date=:today where         phone=:phone"),
            {"today" : data['today'],
              "phone": data['phone']}
    )



def gas_bill_db(data):
  with engine.connect() as conn:
    result = conn.execute(
          text("select * from gas where phone=:phone"),
            {"phone": data['phone']}
    )
    rows = []
    rows=[dict(zip(result.keys(), row)) for row in result]
      
    if len(rows) == 0:
      with engine.connect() as conn:
        query = text("INSERT INTO gas (id, phone, email, curr_date) VALUES (:id, :phone, :email, :curr_date)")

        conn.execute(query, { 
                 'id':data['id'],
                 'phone':data['phone'],
                 'email':data['email'],                 
                 'curr_date':data['today'],
                 
        })
        water_bill_db(data)
    
    else:
      conn.execute(
          text("update gas set curr_date=:today where         phone=:phone"),
            {"today" : data['today'],
              "phone": data['phone']}
      )
      return (rows[0])



def update_gas_last_bill_date(data):
  with engine.connect() as conn:
    conn.execute(
          text("update gas set last_bill_date=:today where         phone=:phone"),
            {"today" : data['today'],
              "phone": data['phone']}
    )



def elec_bill_db(data):
  with engine.connect() as conn:
    result = conn.execute(
          text("select * from elec where phone=:phone"),
            {"phone": data['phone']}
    )
    rows = []
    rows=[dict(zip(result.keys(), row)) for row in result]
    if len(rows) == 0:
      with engine.connect() as conn:
        query = text("INSERT INTO elec (id, phone, email, curr_date) VALUES (:id, :phone, :email, :curr_date)")

        conn.execute(query, { 
                 'id':data['id'],
                 'phone':data['phone'],
                 'email':data['email'],                 
                 'curr_date':data['today'],
                 
        })
        elec_bill_db(data)

    else:
      update_curr_date(data)
      return (rows[0])
      

def update_elec_last_bill_date(data):
  with engine.connect() as conn:
    conn.execute(
          text("update elec set last_bill_date=:today where         phone=:phone"),
            {"today" : data['today'],
              "phone": data['phone']}
    )

def update_curr_date(data):
  with engine.connect() as conn:
    conn.execute(
          text("update elec set curr_date=:today where         phone=:phone"),
            {"today" : data['today'],
              "phone": data['phone']}
    )