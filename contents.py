import sqlite3


def connect(dbname):
    conn=sqlite3.connect(dbname)
    conn.execute("CREATE TABLE hotel_info (hotel_name TEXT, hotel_reviews_count varchar(100),hotel_features text,hotel_price varchar(50))")
    print("Table created successfully")
    conn.close()

def insert_into_table(dbname,values):
    conn=sqlite3.connect(dbname)
    print("Inserted into table"+str(values))
    insert_sql="INSERT INTO hotel_info VALUES(?,?,?,?)"
    conn.execute(insert_sql,values)
    conn.commit()
    conn.close()
    
def get_Hotel_info(dbname):
    conn=sqlite3.connect(dbname)
    cur=conn.cursor()
    cur.execute("SELECT * FROM hotel_info ")
    table_data=cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()
