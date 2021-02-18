# DE positives
import pandas as pd
from datetime import datetime 

def main():
	print("\n\nRun at:", datetime.now())
	df = pd.read_csv('https://myhealthycommunity.dhss.delaware.gov/locations/state/download_covid_19_data')
	df = df[df['Unit'] == 'tests'].set_index(['Year', 'Month', 'Day']).sort_index()
	print(df.loc[df.index.unique()[-3]][['Statistic', 'Value']])

if __name__ == "__main__":
    main()
