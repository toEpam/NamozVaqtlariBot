import httpx
from bs4 import BeautifulSoup


async def get_prayer_tymes(region):
    response = httpx.get(f"https://namozvaqti.uz/shahar/{region}")
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    return [nam.text for nam in soup.find_all('p', {"class": "time"})]
