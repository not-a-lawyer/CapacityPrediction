import unittest
from crawler import *



class MyTestCase(unittest.TestCase):
    def test_getting_site_content(self):
        soup = crawl_url("https://member.superfit.club/CheckinCounter/GetClubsCheckinCounterPage")
        result = process_soup(soup)
        pass