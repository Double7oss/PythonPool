# Python - 0 - Starting

Collection of 42-style warm‑up exercises that revisit Python basics, IO, control flow, re‑implementations of builtins, and simple packaging. Each subfolder (`ex00` … `ex09`) is self‑contained and can be run directly with `python3` from the repository root.

## Requirements
- Python 3.10+ (standard library only, except for the optional `tqdm` import in `ex08`)
- `pip` (only needed if you want to build or install the package in `ex09`)

Create and activate a virtual environment if you want to keep things isolated:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

## Exercises

| Folder | Topic | What it does | Run it with |
| ------ | ----- | ------------ | ----------- |
| `ex00/Hello.py` | Data structures | Builds list/tuple/set/dict variants of “Hello” strings and prints them. | `python3 ex00/Hello.py` |
| `ex01/format_ft_time.py` | Time & formatting | Formats seconds since epoch in fixed and scientific notation plus a human date. | `python3 ex01/format_ft_time.py` |
| `ex02/find_ft_type.py` | Type inspection | `all_thing_is_obj` reports the concrete type of the provided object. | `python3 ex02/test.py` (or import the function) |
| `ex03/NULL_not_found.py` | Truthy/falsey values | Classifies `None`, `nan`, zero, empty strings, and booleans with custom messages. | `python3 ex03/test.py` |
| `ex04/whatis.py` | CLI & assertions | Validates a single integer argument and prints whether it is even or odd. | `python3 ex04/whatis.py 42` |
| `ex05/building.py` | Text analysis | Counts uppercase, lowercase, digits, spaces, and punctuation in user input or CLI arg. | `python3 ex05/building.py "Some text!"` |
| `ex06/filterstring.py` | Re‑implementing `filter` | Custom `ft_filter` returns filtered lists; `filterstring.py` keeps words longer than _n_. | `python3 ex06/filterstring.py "hello world" 4` |
| `ex07/sos.py` | Morse encoder | Converts alphanumeric strings (and spaces) into Morse code, validating inputs. | `python3 ex07/sos.py "sos 42"` |
| `ex08/Loading.py` | Iterators & UX | `ft_tqdm(range(...))` yields items while printing a dynamic progress bar. | `python3 -i ex08/Loading.py` then iterate over `ft_tqdm(range(100))` |
| `ex09/ft_package` | Packaging | Minimal `count_in_list` package with `setup.py`, tests, and metadata. | `pip install ./ex09/ft_package` then `python3 ex09/ft_package/tester.py` |

## Working with `ex09/ft_package`
1. Install locally: `pip install ./ex09/ft_package`
2. Verify: `python3 ex09/ft_package/tester.py` (expects outputs `2` and `0`)
3. Build artifacts: from `ex09/ft_package`, run `python3 -m build` (requires `build` extra; install via `pip install build` if needed).

## Tips
- Every script performs its own argument validation and prints descriptive assertion errors; read the message if something fails.
- Most exercises are standalone functions—feel free to import them into a Python shell to experiment beyond the provided tests.
- Keep the repo root (`Python - 0 - Starting`) on your `PYTHONPATH` if you want to run modules with `python -m ex0x.module`.
