import re
import requests
from bs4 import BeautifulSoup

URL = "https://www.ezoic.com"
page = requests.get(URL, timeout=5)

soup = BeautifulSoup(page.content, "html.parser")
links = soup.find_all("a")

external_link = re.compile(r"^https?:\/\/([a-z0-9\.-]+)", flags=re.IGNORECASE)
found_domains = set()

for a in links:
  href = a.get('href')
  domain = re.findall(external_link, href)
  if domain:
    found_domains.add(domain[0])

print(found_domains)