from test_task1.matrix_parser import parce_matrix


def test_parce_matrix(matrix_fixtures):
    for fixture_name in matrix_fixtures:
        matrix_text = matrix_fixtures[fixture_name]["text"]
        matrix_list = matrix_fixtures[fixture_name]["list"]
        result = parce_matrix(matrix_text)
        error = f"For fixture {fixture_name}, expected {matrix_list}, " \
                f"but got {result}"
        assert result == matrix_list, error
