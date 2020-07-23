import requests
from bs4 import BeautifulSoup


def crawl_url(url):
    """

    :param url:
    :return: returns Soup object of website

    """

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def process_soup(soup):
    """

    :param soup:
    :return: a tuple list with people capacity and district name
    """
    found_h4 = soup.find_all("h4")
    found_label = soup.find_all("label")

    results = []
    for i in range(10):
        # match every first and every entry of label entry with all even h4 entries
        results.append((found_label[2 * i + 1], found_h4[i + 1]))


