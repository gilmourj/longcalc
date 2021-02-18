# HI PCR Test Encounters
import pandas as pd
import requests
from datetime import datetime, timezone
from pytz import timezone as tz  # replace with ZoneInfo once G upgrades to 3.9

def main():
	print("\n\nRun at:", datetime.now())
	hi = pd.read_csv("https://public.tableau.com/views/EpiCurveApr4/CSVDownload.csv?:showVizHome=no")
	print(hi.select_dtypes(exclude=['object']).sum())

	# HI updated time
	res = requests.get("https://services9.arcgis.com/aKxrz4vDVjfUwBWJ/arcgis/rest/services/HIEMA_TEST_DATA_PUBLIC_LATEST/FeatureServer/0/query?where=name%3D'State'&returnGeometry=false&outFields=*&orderByFields=reportdt desc&resultOffset=0&resultRecordCount=1&f=json")
	updated = datetime.fromtimestamp(res.json()['features'][0]['attributes']['reportdt']/1000) # because ms
	# format we want: 12/27/2020 8:30:00
	print("\nUpdate time: ", updated.replace(tzinfo=timezone.utc).astimezone(tz=tz("Pacific/Honolulu")).strftime("%m/%d/%Y %H:%M:%S"))

if __name__ == "__main__":
    main()
