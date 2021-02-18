# WV Testing
import pandas as pd
from datetime import datetime

def main(): 
    print("Last run at: ", datetime.now().isoformat())
    wv = pd.read_csv("https://raw.githubusercontent.com/COVID19Tracking/covid19-datafetcher/data/wv_lab_tests.csv", thousands=",")
    print(wv.loc[:, wv.columns != 'date'].sum(axis=0))

if __name__ == "__main__":
    main()
