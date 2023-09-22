import mysql.connector as mc
# from connection_constants import *

query="INSERT INTO registered_user(sample_id,customer_name, entry_date ,submitter_type, contact ,address_line_1,city_village,district,pincode,product,parameter) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s)"

def db_connection():
    global conn
    conn=mc.connect(
        host="localhost",
        user="root",
        password="hare.krishna@98",
        database="chemometrics_lab"
        )
    

def insert_data(query=None,data=None):
    global cur,conn
    try:
        cur=conn.cursor()
        insert_script  = query
        insert_values = data
        cur.execute(insert_script, insert_values)

        conn.commit()
        print("code run sucessfully.")

    except Exception as error:
        print(error)

    finally:
        if cur is None:
            cur.close()
        if conn is None:
            conn.close()

# if __name__=='__main__':
#     db_connection()
#     insert_data(query=query,data=(1,"x","y","z","a","b","c","d","e","f","g"))

