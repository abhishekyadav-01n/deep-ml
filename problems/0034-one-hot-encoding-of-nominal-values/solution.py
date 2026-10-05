import numpy as np

def to_categorical(x, n_col=None):
	if n_col == None:
		n_col = np.max(x) + 1

	result = []

	for i in range(len(x)):
		row = []
		for j in range(n_col):
			if(j == x[i]):
				row.append(1)
			else:
				row.append(0)
		result.append(row)
	
	return result
	pass