# FizzBuzz

Simple FizzBuzz CLI application. You will get better at Python programming by reading this code and understanding it.

## Installation

```shell
# Clone the repository
git clone git@github.com:shunsock/fizzbuzz.git

# Change the directory
cd fizzbuzz

# Install uv (If you haven't already)
# @see: https://github.com/astral-sh/uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Python 3.12.0
uv python install 3.12.0
uv python pin 3.12.0

# Install the dependencies
uv sync
```

## Getting Started

You can run the application by using `uv` command.

```shell
# Run the application
uv run app/main.py -h
```

also, you can use `Taskfile` to run the application. (Of course, you need to install `task`)

```shell
# Run the application
task run -- -h
```

## Usage

```shell
usage: main.py [-h] [--start START] [--end END]

FizzBuzz CLI

options:
  -h, --help     show this help message and exit
  --start START  The start of the FizzBuzz sequence
  --end END      The upper bound for the FizzBuzz sequence
```

## Test

You can check the python code with following command.

```shell
# Run linting, static analysis and test
task validate
```

see also

- [ruff](https://github.com/astral-sh/ruff)
- [mypy](https://github.com/python/mypy)
- [pytest](https://github.com/pytest-dev/pytest)
- [coverage](https://github.com/nedbat/coveragepy)

## License

[MIT](LICENSE)
