import psycopg2 as psycopg2


def connect_data():

    conn = psycopg2.connect("dbname=capacity")
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor, command):
    cursor.execute(command)

def add_data_to_db(data):
    conn, cursor = connect_data()
    for i in range(len(data)):
        capacity = data[i][0]
        district = data[i][1]
        color = data[i][2]
        cursor.execute("INSERT INTO entries (district_name, capacity, color) VALUES (%s, %s, %s)", (district, capacity, color))
    conn.commit()