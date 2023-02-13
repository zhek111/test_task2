import pytest
from aioresponses import aioresponses
from test_task1.matrix_loader import load_matrix
from tests import matrix_fixtures  # noqa: F401


@pytest.mark.asyncio
async def test_load_matrix(matrix_fixtures):  # noqa: F811
    url = "https://raw.githubusercontent.com/avito-tech/python-trainee" \
          "-assignment/main/matrix.txt"
    expected_output = matrix_fixtures["matrix_4x4"]["text"]

    with aioresponses() as m:
        m.get(url, body=matrix_fixtures["matrix_4x4"]["text"])
        result = await load_matrix(url)
        assert result == expected_output
