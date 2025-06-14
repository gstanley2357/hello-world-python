# Hello World Application

This is a simple Python application that demonstrates a functional approach to generating greeting messages. The application includes a function that returns a greeting based on the input provided.

## Project Structure

```
hello_world_app
├── src
│   ├── hello.py
├── tests
│   └── test_hello.py
├── requirements.txt
└── README.md
```

## Getting Started

To get started with this application, follow the instructions below.

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd hello_world_app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

To use the greeting function, you can import it from the `hello.py` file in the `src` directory. Here is an example of how to use it:

```python
from src.hello import greet

print(greet())  # Outputs: Hello, world!
print(greet("Alice"))  # Outputs: Hello, Alice!
```

### Running Tests

To run the unit tests for this application, use the following command:

```
pytest tests/test_hello.py
```

Make sure you have `pytest` installed, which can be done via the `requirements.txt`.

## License

This project is licensed under the MIT License. See the LICENSE file for details.