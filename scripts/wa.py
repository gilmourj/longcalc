# WA
import pandas as pd
from datetime import datetime

def main():
	print("\n\nRun at: ", datetime.now())
	wa_link = 'https://www.doh.wa.gov/Portals/1/Documents/1600/coronavirus/data-tables/PUBLIC_Tests_by_Specimen_Collection.xlsx'
	print("Link = ", wa_link)

	wa = pd.read_excel(wa_link, sheet_name = 'State').filter(regex='(Positive|Negative)').drop(columns='Positive tests (%)')
	wa.columns = [x.split()[0] for x in wa.columns]
	wa.groupby(wa.columns.values, axis=1).sum().sum()

if __name__ == "__main__":
    main()
