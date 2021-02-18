# MI Testing
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def main():
	print("\n\nRun at: ", datetime.now())
	url = 'https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html'

	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'html.parser')
	a = soup.find('a', string="Diagnostic Tests by Result and County")
	mi_link = "https://www.michigan.gov/{}".format(a['href'])
	print("Link = ", mi_link)

	mi = pd.read_excel(mi_link).drop(columns=['COUNTY'])
	print(mi.sum())

if __name__ == "__main__":
    main()
