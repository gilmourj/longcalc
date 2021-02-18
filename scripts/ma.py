# MA
from io import StringIO, BytesIO
from bs4 import BeautifulSoup
import pandas as pd
import re
import requests
import zipfile
from datetime import datetime


def main():
	print("\n\nRun at:", datetime.now())
	url = 'https://www.mass.gov/info-details/covid-19-response-reporting'
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'html.parser')
	a = soup.find('a', string=re.compile("COVID-19 Raw Data"))
	link = "https://www.mass.gov{}".format(a['href'])
	print("Download link = ", link)

	res = requests.get(link)
	tabs = pd.read_excel(res.content, sheet_name=None)

	print("PCR Total People")
	print(tabs['Testing2 (Report Date)']['Molecular Total'].iloc[-1], "\n")

	df = tabs['TestingByDate (Test Date)'].filter(like="All Positive")
	print(df.sum())

	# weekly report
	url = 'https://www.mass.gov/info-details/covid-19-response-reporting'
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'html.parser')
	a = soup.find('a', string=re.compile("Weekly Public Health Report - Raw"))
	link = "https://www.mass.gov{}".format(a['href'])
	print("\nWeekly link = ", link)
	res = requests.get(link)
	df = pd.read_excel(BytesIO(res.content), sheet_name='Antibody', parse_dates=['Test Date'], index_col='Test Date')
	print(df.sum())

	# ever hospitalized
	print('\nEver Hospitalized')
	max_date = tabs['RaceEthnicityLast2Weeks']['Date'].max()
	print(tabs['RaceEthnicityLast2Weeks'][tabs['RaceEthnicityLast2Weeks']['Date'] == max_date].sum())

if __name__ == "__main__":
    main()
