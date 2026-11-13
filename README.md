# PCEP Exam Preparation (Python-PCEP)

Practice scripts and notes for the PCEP-30-02 syllabus. Each numbered file is a short Python example for one syllabus topic, with a matching practice file in blocks 1 and 2. The goal is to read the task in the module docstring, run the file, and compare the printed result with the code.

Syllabus and style references used by these notes:

- [Official PCEP syllabus](https://pythoninstitute.org/pcep-exam-syllabus)
- [Python 3.12 standard library](https://docs.python.org/3.12/library/index.html)
- [PEP 8](https://peps.python.org/pep-0008/)

`PE1_Study_Guide.md` is a separate set of runnable snippets covering tuple concatenation, `input()` returning a string, modulo, `SyntaxError` patterns, and `range()` direction.

## Prerequisites

- Python 3. The notebooks record `language_info` version 3.8. The lesson scripts below were run with Python 3.12.3.
- A shell that can run `python3`.
- The lesson modules use only the standard library (`math`, `random`, `sys`, `time`).
- `block2/pypi-scrape/fetch-package-names.py` and `block2/pypi-scrape/extract_pypi_maintainer_emails.py` import the third-party package `requests`. This repository does not ship a requirements file. `python3 -c "import requests"` fails until that package is installed in the environment you use.

## Install, build, run, and test

There is no package install, no build step, and no automated test suite. `.gitignore` ignores `__pycache__/`, `.pytest_cache/`, `*.pyc`, `*.swp`, and `.env`. No pytest files are in the tree.

Check that every Python file compiles:

```bash
python3 -m py_compile block1/*.py block2/*.py block3/*.py block4/*.py block2/pypi-scrape/*.py
```

Run one lesson module from the repository root:

```bash
python3 block1/1_1_fundamentals.py
```

Run every module that does not wait for keyboard input:

```bash
python3 block1/1_1_fundamentals.py
python3 block1/1_1_practice.py
python3 block1/1_2_logic_structure.py
python3 block1/1_2_practice.py
python3 block1/1_3_literals_variables.py
python3 block1/1_4_operators.py
python3 block2/2_1_branching.py
python3 block2/2_2_loops.py
python3 block2/2_2_practice.py
python3 block3/3_1_lists.py
python3 block3/3_2_tuples.py
python3 block3/3_3_dictionaries.py
python3 block3/3_4_strings.py
python3 block4/4_1_functions.py
python3 block4/4_2_function_environment.py
python3 block4/4_3_exceptions_hierarchy.py
python3 block4/4_4_exception_handling.py
python3 block1/1_5_practice.py
```

`block1/1_5_practice.py` reads `/etc/services` and `/etc/passwd` on the machine where you run it, prints each service line, and prints each username separated by commas.

`block3/3_4_strings.py` compiles and runs. Python 3.12 prints `SyntaxWarning: invalid escape sequence '\)'` because the module docstring contains `\`.

`block2/2_2_practice.py` prints a progress bar and sleeps about 0.1 seconds per step, so it takes a few seconds.

Modules that call `input()` need a line on stdin. Examples:

```bash
printf '1337\n' | python3 block1/1_3_practice.py
printf '==\n' | python3 block1/1_4_practice.py
printf '25\n3.5\n' | python3 block1/1_5_io_operations.py
printf 'explore\n' | python3 block2/2_1_practice.py
```

`block1/1_4_practice.py` accepts one of `~`, `&`, `^`, `|`, `>>`, `<<`, `==`, `!=`, `<`, `>`, `**`, `//`, or `%`. `>>` and `<<` then ask for an integer offset. `block2/2_1_practice.py` accepts `call for help`, `explore`, or `rest`.

The notebooks `loops.ipynb`, `tuples.ipynb`, and `dictionaries.ipynb` are Jupyter notebooks (kernel display name `Python (Pyodide)`). Open them in a Jupyter client. This repository does not include a notebook runner. The files are valid JSON:

```bash
python3 -c 'import json; json.load(open("loops.ipynb")); json.load(open("tuples.ipynb")); json.load(open("dictionaries.ipynb"))'
```

From `block2/pypi-scrape`, print package names already saved in `pypi_simple.txt` (the script opens that filename in the current directory):

```bash
cd block2/pypi-scrape
python3 parse-package-names.py
```

`fetch-package-names.py` downloads `https://pypi.org/simple/` and writes `pypi_simple.txt` in the current directory. It needs `requests`. `extract_pypi_maintainer_emails.py` reads the public PyPI index and package metadata and prints maintainer or author email addresses. Both of those scripts are outside the numbered lesson modules.

## Usage

Work through the blocks in order. Each `*_practice.py` file restates the task from the matching lesson file.

### Block 1: Computer programming and Python fundamentals

| File | What it covers |
| --- | --- |
| `block1/1_1_fundamentals.py`, `block1/1_1_practice.py` | Interpretation, compilation, lexis, syntax, and semantics (comments). `1_1_practice.py` prints nothing. |
| `block1/1_2_logic_structure.py`, `block1/1_2_practice.py` | Comments, keywords, indentation, and a function. The practice file builds a random dotted address and prints its classful class and subnet mask. |
| `block1/1_3_literals_variables.py`, `block1/1_3_practice.py` | Boolean, binary, octal, hex, scientific float, and string values. The practice file also uses `math.sqrt` and `input()`. |
| `block1/1_4_operators.py`, `block1/1_4_practice.py` | `**`, `//`, `%`, bitwise operators, and relational operators. The practice file waits for `input()`. |
| `block1/1_5_io_operations.py`, `block1/1_5_practice.py` | `print()` with `sep` and `end`, and casting `input()` to `int` and `float`. The practice file reads `/etc/services` and `/etc/passwd`. |

### Block 2: Control flow

| File | What it covers |
| --- | --- |
| `block2/2_1_branching.py`, `block2/2_1_practice.py` | `if`, `elif`, `else`, and a nested condition. The practice file reads a dungeon choice from `input()`. |
| `block2/2_2_loops.py`, `block2/2_2_practice.py` | `for`, `range()`, `break`, `continue`, and a `while`/`else` loop. The practice file draws a progress bar. |

### Block 3: Data collections

| File | What it covers |
| --- | --- |
| `block3/3_1_lists.py` | Indexing, slicing, `append()`, `insert()`, a list comprehension, and a nested list. |
| `block3/3_2_tuples.py` | Indexing, a `TypeError` on item assignment, and a tuple nested in a list. |
| `block3/3_3_dictionaries.py` | `keys()`, `values()`, `items()`, and a loop over pairs. |
| `block3/3_4_strings.py` | Indexing, slicing, `\n` and `\t`, and a multi-line string. |

`loops.ipynb` exercises lists (aliasing, slicing, `insert`, membership, and comprehensions). `tuples.ipynb` exercises tuple concatenation, `count`, `index`, slicing, and `sorted`. `dictionaries.ipynb` exercises a dict of init systems, `keys()`, `values()`, `items()`, and `get()`. Some notebook cells are blank or contain unfinished expressions.

### Block 4: Functions and exceptions

| File | What it covers |
| --- | --- |
| `block4/4_1_functions.py` | A function that returns a value, and a recursive factorial. |
| `block4/4_2_function_environment.py` | Positional arguments, keyword arguments, default parameters, and `global`. |
| `block4/4_3_exceptions_hierarchy.py` | `IndexError`, `KeyError`, and `ValueError`, each caught and printed. |
| `block4/4_4_exception_handling.py` | `try`, `except`, `else`, and `finally` around division. |

## Layout

```text
block1/                 Block 1 lesson and practice scripts
block2/                 Block 2 lesson and practice scripts
block2/pypi-scrape/     Local PyPI simple-index notes and scripts
block3/                 Block 3 lesson scripts
block4/                 Block 4 lesson scripts
loops.ipynb             List notebook
tuples.ipynb            Tuple notebook
dictionaries.ipynb      Dictionary notebook
PE1_Study_Guide.md      Extra pattern notes
```

## License

This repository has no `LICENSE` file.
