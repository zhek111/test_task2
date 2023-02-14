import aiohttp
import pytest
import requests
from aiohttp import ClientError
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
async def test_non_existent_site(requests_mock):
    with pytest.raises(expected_exception=Exception):
        requests_mock.get(
            'https://ru.hexlettt.io/courses')
        await load_matrix('https://ru.hexlettt.io/courses')

