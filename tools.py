import pandas as pd

def get_data(name):
	data = pd.read_csv(name, sep='\t')
	data = data.iloc[:,49:125]
	return data

def get_subsets(set):
	return (set[0:1000, 0:5], set[1000::, 5:10])

def get_Ysubset(set):
    return (set[0:1000], set[1000::])