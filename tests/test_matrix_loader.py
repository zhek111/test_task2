import pytest
from aioresponses import aioresponses
from test_task1.matrix_loader import load_matrix


@pytest.mark.asyncio
async def test_load_matrix(matrix_fixtures):
    url = "https://raw.githubusercontent.com/avito-tech/python-trainee" \
          "-assignment/main/matrix.txt"
    expected_output = matrix_fixtures["matrix_4x4"]["text"]

    with aioresponses() as m:
        m.get(url, body=matrix_fixtures["matrix_4x4"]["text"])
        result = await load_matrix(url)
        assert result == expected_output


@pytest.mark.asyncio
async def test_load_matrix_404(matrix_fixtures):
    url = "https://raw.githubusercontent.com/avito-tech/python-trainee" \
          "-assignment/main/matrix.txt"
    with aioresponses() as m:
        m.get(url, status=404)
        with pytest.raises(Exception, match='Client error'):
            await load_matrix(url)


@pytest.mark.asyncio
async def test_load_matrix_500(matrix_fixtures):
    url = "https://raw.githubusercontent.com/avito-tech/python-trainee" \
          "-assignment/main/matrix.txt"
    with aioresponses() as m:
        m.get(url, status=500)
        with pytest.raises(Exception, match='Server error'):
            await load_matrix(url)
