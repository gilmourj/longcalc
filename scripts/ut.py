# UT 
from io import StringIO, BytesIO
import pandas as pd
import requests
import zipfile
from datetime import datetime

def main():
    print("\n\nRun at: ", datetime.now())
    url = 'https://coronavirus-dashboard.utah.gov/Utah_COVID19_data.zip'
    res = requests.get(url)
    zipdata = BytesIO(res.content)
    zip = zipfile.ZipFile(zipdata, 'r')
    for zf in zip.filelist:
      if zf.filename.startswith('Overview_Total Tests by Date'):
        # yay, the testing file
        title = 'Tests'
      elif zf.filename.startswith('Overview_Number of People Tested by Date'):
        title = 'People'
      else:
        title = None
      if title:
        title = "Metrics for {} (from {})".format(title, zf.filename)
        print(title, "\n"+"="*len(title))
        df = pd.read_csv(zip.open(zf.filename)).drop(columns=[' Total Daily Tests', 'Total Positive Tests', 'Daily People Tested', 'Daily Positive Tests'], errors="ignore")
        print(df.groupby(['Test Type', 'Result']).sum())

if __name__ == "__main__":
    main()
