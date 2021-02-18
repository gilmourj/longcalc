# WI PCR Testing Encounters
import pandas as pd
from datetime import datetime

def main():
	print("Run at: ", datetime.now())
	wi = pd.read_csv("https://bi.wisconsin.gov/t/DHS/views/PercentPositivebyTestPersonandaComparisonandTestCapacity/TestCapacityDashboard.csv", thousands=",")
	print("PCR Testing Encounters: " + str(wi[wi['Measure Names'] == 'Total people tested daily']['Number of Tests'].sum()))

if __name__ == "__main__":
    main()
