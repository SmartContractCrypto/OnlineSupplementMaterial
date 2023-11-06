import pandas as pd
from collections import Counter


contracts = pd.read_csv("../data/1_CryptoContracts_Label.CSV")

# Contract Number
print("Contract Number:",len(set(contracts['address'])))

# Number of Crypto Tasks
print("Number of Crypto Tasks:", dict(Counter(contracts['Crypto Task'])))
