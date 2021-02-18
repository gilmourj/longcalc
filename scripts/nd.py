# ND Negatives + Testing
import pandas as pd
import requests
from io import StringIO
from datetime import datetime

def main():
	print("\n\nRun at: ", datetime.now())
	url = "https://static.dwcdn.net/data/NVwou.csv"
	headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0"}
	req = requests.get(url, headers=headers)
	print(pd.read_csv(StringIO(req.text)).filter(like='Negative').sum())

	print("\n")
	print("Testing Data")
	df = pd.read_csv('https://www.health.nd.gov/sites/www/files/documents/Files/MSS/coronavirus/charts-data/PublicUseData.csv')
	print(df.filter(like='tests').sum())

if __name__ == "__main__":
    main()
