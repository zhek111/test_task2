from test_task1.matrix_traversal_base import \
    matrix_counter_clock_spiral_traversal


def test_matrix_counter_clock_spiral_traversal(matrix_fixtures):
    for fixture_name in matrix_fixtures:
        matrix_list = matrix_fixtures[fixture_name]["list"]
        expected_traversal = matrix_fixtures[fixture_name]["traversal"]
        result = matrix_counter_clock_spiral_traversal(matrix_list)
        error = f"For fixture {fixture_name}, " \
                f"expected {expected_traversal}, but got {result}"
        assert result == expected_traversal, error
