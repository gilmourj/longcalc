# NC Antigen tests
import pandas as pd
from datetime import datetime

def main():
	print("\n\nRun at: ", datetime.now())
	nc = pd.read_csv("https://public.tableau.com/views/NCDHHS_COVID-19_DataDownload/DailyTestingMetrics.csv", parse_dates=['Date'], index_col='Date', thousands=',')
	print(nc.pivot(columns='Measure Names').sum().astype('int64'))

if __name__ == "__main__":
    main()
