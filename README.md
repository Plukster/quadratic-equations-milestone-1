# Quadratic Equations - Milestone 1

## Back to School

This project demonstrates solving quadratic equations with coefficients that may have formatting issues (extra spaces, missing spaces).

### Project Structure
```
milestone_1/
└── equations.py
```

### What This Does

The `equations.py` file contains a simple quadratic equation solver that:
- Parses quadratic equations in the format: `ax² + bx + c = 0`
- Extracts coefficients (a, b, c) from the equation string
- Solves using the quadratic formula: `x = (-b ± √(b² - 4ac)) / (2a)`
- Handles both real and complex solutions

### Example Usage

```python
# Simple quadratic equation solver
eq = '4x^2 +4x + (-8) = 0'
# Output:
# a = 4, b = 4, c = -8
# x1 = 1.0
# x2 = -2.0
```

### Requirements

- Python 3.x
- No external dependencies (uses built-in `cmath` module)

### How to Run

```bash
cd milestone_1
python equations.py
```