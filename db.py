import sqlite3

# sql = """CREATE TABLE names(
#     name TEXT,
#     description TEXT);"""

def set_data_to_db(name,description):
    con = sqlite3.connect("./names.db", check_same_thread=False)
    cur = con.cursor()
    try:
        sql = f"""INSERT INTO names(name,description)
            VALUES('{name}','{description}');"""
        cur.execute(sql)
    except sqlite3.DatabaseError as e:
        print(e)
        return "Error"
    else:
        print("OK")
        con.commit()
        cur.close()
        con.close()
        return "Success"
    
def get_data_from_db(letter):
    con = sqlite3.connect("./names.db", check_same_thread=False)
    cur = con.cursor()
    
    try:
        first_letter = letter.upper()
        query = f"SELECT * FROM names WHERE name LIKE '{first_letter}%'"
        data = cur.execute(query)
        return data.fetchall()
    except sqlite3.DatabaseError as e:
        print(e)
    else:
        print("OK")

def search_meaning_name(name):
    con = sqlite3.connect("./names.db", check_same_thread=False)
    cur = con.cursor()
    
    try:
        query = f"SELECT * FROM names WHERE name LIKE '{name}%'"
        data = cur.execute(query)
        return data.fetchall()
    except sqlite3.DatabaseError as e:
        print(e)
    else:
        print("OK")