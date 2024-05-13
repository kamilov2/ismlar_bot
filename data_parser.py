import requests
import time
from bs4 import BeautifulSoup
from db import set_data_to_db


HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

for i in range(1,100):
    url = f"https://ismlar.com/category/Fors-tojikcha?page={i}"
    page = requests.get(url=url,headers=HEADERS)
    soup = BeautifulSoup(page.text, "html.parser")
    ul = soup.find("ul", class_="list-none space-y-2")
    for li in ul.find_all("li"):
        name = li.find("a")
        description = li.find("p")
        # print(name,description)
        print(set_data_to_db(name.text.strip(),description.text.strip()))

    time.sleep(1)
    print(f"OK page={i}")
    