import re
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == "__main__":
    base_url = "https://www.sacred-texts.com/neu/ascp/"
    response = urlopen(base_url)

    soup = BeautifulSoup(response, "lxml")

    for link in soup.find_all('a'):
        page_title = link.get('href')
        if "a" in page_title:
            page_response = urlopen(base_url + page_title)
            file_title = re.sub(".htm", "", page_title)
            page_soup = BeautifulSoup(page_response, "lxml")
            with open("data/" + file_title + ".txt", "w", encoding="utf-8") as file:
                body_text = page_soup.get_text()
                body_text = body_text.strip()
                file.write(body_text)
        time.sleep(1) #So as not to overburden the server