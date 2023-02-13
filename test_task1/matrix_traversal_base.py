def matrix_counter_clock_spiral_traversal(
        matrix: list[list[int]]) -> list[int]:
    size = current_row = len(matrix)
    start_point = current_column = current_item = 0
    result = []
    while current_row > 0:
        for current_item in range(start_point, current_row):
            result.append(matrix[current_item][current_column])
        current_row -= 1
        current_column = current_item
        if current_row > 0:
            for current_item in range(size - current_row, current_row + 1):
                result.append(matrix[current_column][current_item])
            for current_item in range(current_column - 1,
                                      size - current_row - 2, -1):
                result.append(matrix[current_item][current_column])
        else:
            break
        current_column = current_item
        current_row -= 1
        if current_row > 0:
            for current_item in range(current_row, size - current_row - 2, -1):
                result.append(matrix[current_column][current_item])
            current_column, current_row = current_column + 1, current_row + 1
            start_point += 1
        else:
            break
    return result
