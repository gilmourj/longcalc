# ME 
import pandas as pd
from datetime import datetime

def main():
	print("\n\nRun at: ", datetime.now())
	print(pd.read_csv("https://gateway.maine.gov/dhhs-apps/mecdc_covid/hospital_capacity.csv", nrows=1, usecols=[0,1,2,3]))

if __name__ == "__main__":
    main()
