name: Python package

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.7", "3.8", "3.9", "3.10", "3.11"]

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install ruff pytest
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      - name: Lint with ruff
        run: |
          # stop the build if there are Python syntax errors or undefined names
          ruff --format=github --select=E9,F63,F7,F82 --target-version=py37 .
          # default set of ruff rules with GitHub Annotations
          ruff --format=github --target-version=py37 .
      - name: Test with pytest
        run: |
          pytest
