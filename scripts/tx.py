# TX
import pandas as pd
import requests
from datetime import datetime, timedelta

def main():
    print("\n\nRun at: ", datetime.now())
    url = 'https://www.dshs.texas.gov/coronavirus/TexasCOVID-19HospitalizationsOverTimebyTSA.xlsx'
    df = pd.read_excel(url, sheet_name='COVID-19 ICU', skiprows=2)
    print("ICU")
    print(df.loc[df[df.columns[0]] == 'Total'][df.columns[-1]])
    
    # PCR Positives
    res = requests.get('https://services5.arcgis.com/ACaLB9ifngzawspq/arcgis/rest/services/TX_DSHS_COVID19_TestData_Service/FeatureServer/6/query?where=1%3D1&outStatistics=%5B%7B%27statisticType%27%3A+%27sum%27%2C+%27onStatisticField%27%3A+%27NewPositive%27%7D%2C+%7B%27statisticType%27%3A+%27sum%27%2C+%27onStatisticField%27%3A+%27OldPositive%27%7D%5D&f=json')
    print("\nPCR Positives")
    print(sum(res.json()['features'][0]['attributes'].values()))
    
    res = requests.get('https://services5.arcgis.com/ACaLB9ifngzawspq/ArcGIS/rest/services/TX_DSHS_COVID19_Cases_Service/FeatureServer/2/query?where=1%3D1&outFields=%2A&orderByFields=Date+desc&resultRecordCount=1&f=json')
    print("\nCases Timestamp (as-of)")
    cases_date = datetime.fromtimestamp(res.json()['features'][0]['attributes']['Date']/1000)
    # convent to TX time through trickery (from UTC)
    print(cases_date - timedelta(hours=6))
    
    # Antigen Positives
    res = requests.get('https://services5.arcgis.com/ACaLB9ifngzawspq/ArcGIS/rest/services/TX_DSHS_COVID19_TestData_Service/FeatureServer/3/query?where=1%3D1&objectIds=&time=&resultType=none&outFields=*&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&sqlFormat=none&f=json')
    print("\nAntigen Positives")
    print(res.json()['features'][5]['attributes']['Count_'])
    
    # Antibody Positives
    print("\nAntibody Positives")
    print(res.json()['features'][2]['attributes']['Count_'])

if __name__ == "__main__":
    main()
