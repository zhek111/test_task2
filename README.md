# SpiralMatrixTraverser
SpiralMatrixTraverser is a Python library for traversing a matrix in a counter-clockwise spiral order from URL.

## Installation
To install, run:

```bash
git clone git@github.com:zhek111/test_task2.git
cd test_task2
poetry install
```

## Usage

```python
from SpiralMatrixTraverser import get_matrix

traversed_matrix = await get_matrix("https://example.com/matrix.txt")
print(traversed_matrix)
```

## Development
To run linting:
```bash
make lint
```

To run tests:

``` bash
make lint
```
### Modules
##### matrix_loader.py
Contains a function load_matrix which loads a text matrix from a given URL.

#### matrix_parser.py
Contains a function parce_matrix which parses a matrix from a string to list.

#### matrix_traversal_base.py
Contains a function matrix_counter_clock_spiral_traversal which traverses a matrix in a counter-clockwise spiral order.

##### matrix_spiral_traversal.py
This module contains the get_matrix function which demonstrates how to use the SpiralMatrixTraverser library to load a matrix from a given URL, traverse the matrix in a counter-clockwise spiral order, and return the result.

### License
This project is licensed under the terms of the MIT license.

### NOTE
If the ssl=False parameter is passed in the load_matrix function in the matrix_loader.py module, it may be convenient for local use without a certificate, but it may be unsafe when used on the Internet. If you use this library on the Internet, it is recommended to set the ssl=True parameter to ensure a secure connection. For example:
``` bash
async with session.get(url, ssl=True) as response:
    # handle response
```
Please be sure to take appropriate measures to ensure security when using this library in real-world situations.