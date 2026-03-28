# Claude Code Practice Project

This is a learning project used to practice Claude Code workflows.

## Environment
- Python: use `python3` (not `python` — not available on this system)
- No virtual environment or package manager — stdlib only for now

## Project Structure
- `app.py` — core business logic (discount and tax calculations)
- `test_app.py` — tests, run with `python3 test_app.py`

## Conventions
- `discount_percent` and `tax_rate` are always decimals between 0 and 1 (e.g. 0.1 = 10%)
- Functions in `app.py` should be pure and importable — no module-level side effects
- Tests use plain `assert` statements, no testing framework
