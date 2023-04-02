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

