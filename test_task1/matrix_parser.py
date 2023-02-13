def parce_matrix(matrix: str) -> list[list]:
    lines = matrix.strip().split("\n")
    numbers = [line.split("|")[1:-1] for line in lines]
    matrix_list = [[int(num.strip()) for num in row] for row in numbers if row]
    return matrix_list
