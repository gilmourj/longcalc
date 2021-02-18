# OH testing
import requests
import pandas as pd
from datetime import datetime

def main():
	print("\n\nRun at: ", datetime.now())
	key_url = "https://data.ohio.gov/apigateway-secure/data-portal/download-file/cba54974-06ab-4ec8-92bc-62a83b40614e?key=2b4420ffc0c5885f7cd42a963cfda0b489a9a6dff49461e1a921b355ee0424c029cf4ff2ee80c8c82ef901d818d71f9def8cba3651f6595bd6a07e1477438b97bbc5d7ccf7b5b66c154779ce7a4f5b83"
	testing_url = "https://data.ohio.gov/apigateway-secure/data-portal/download-file/2ad05e55-2b1a-486c-bc07-ecb3be682d29?key=e42285cfa9a0b157b3f1bdaadcac509c44db4cfa0f90735e12b770acb1307b918cee14d5d8e4d4187eb2cab71fc9233bda8ee3eed924b8a3fad33aaa6c8915fe6f3de6f82ad4b995c2359b168ed88fa9"
	url = testing_url

	print(pd.read_csv(requests.get(url).json()['url']).filter(like='Daily').sum())

if __name__ == "__main__":
    main()
