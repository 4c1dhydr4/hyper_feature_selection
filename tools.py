import pandas as pd

def get_data(name):
	data = pd.read_csv(name, sep='\t')
	data = data.iloc[:,49:125]
	return data