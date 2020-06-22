import requests
from bs4 import BeautifulSoup


url = "https://www.trade-ideas.com/SingleAlertType/CAVC/Crossed_above_VWAP.html"
request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')

table = soup.find_all("table")[0]
rows = table.find_all("tr")
for row in rows:
    row_list = [x.text for x in row.find_all("td")]
    print(row_list)
