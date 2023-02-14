from test_task1.matrix_loader import load_matrix
from test_task1.matrix_parser import parce_matrix
from test_task1.matrix_traversal_base import \
    matrix_counter_clock_spiral_traversal


async def get_matrix(url: str) -> list[int]:
    matrix_str = await load_matrix(url)
    matrix = parce_matrix(matrix_str)
    traversed_matrix = matrix_counter_clock_spiral_traversal(matrix)
    return traversed_matrix
