def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	means = []

	rows = len(matrix)
	cols = len(matrix[0])

	if(mode == "row"):
		for i in range(rows):
			total = 0
			for j in range(cols):
				total += matrix[i][j]
			
			means.append(total / cols)
	else:
		for j in range(cols):
			total = 0
			for i in range(rows):
				total += matrix[i][j]
			
			means.append(total / rows)

	return means