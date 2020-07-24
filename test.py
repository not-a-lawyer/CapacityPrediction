import unittest
from crawler import *
from database import *



class MyTestCase(unittest.TestCase):
    def test_getting_site_content(self):
        soup = crawl_url("https://member.superfit.club/CheckinCounter/GetClubsCheckinCounterPage")
        result = process_soup(soup)
        add_data_to_db(result)


        pass
    def test_database_connection(self):
        connection, cursor = connect_data()
        create_table(cursor,
        """CREATE TABLE entries (
            entry_id SERIAL PRIMARY KEY,
            district_name VARCHAR(255) NOT NULL,
            capacity INTEGER NOT NULL,
            color VARCHAR(255) NOT NULL,
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP(0) 
        )"""
        )
        cursor.close()
        connection.commit()
        connection.close()
