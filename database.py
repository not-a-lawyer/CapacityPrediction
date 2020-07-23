import psycopg2 as psycopg2


def connect_data():

    conn = psycopg2.connect("dbname=suppliers user= password=")