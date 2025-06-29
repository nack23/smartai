from sympy import symbols, Eq, solve, simplify
from sympy.parsing.sympy_parser import parse_expr

def solve_math(question):
    x = symbols('x')  # Add more symbols as needed
    try:
        if '=' in question:
            lhs, rhs = question.split('=')
            eq = Eq(parse_expr(lhs), parse_expr(rhs))
            sol = solve(eq)
        else:
            expr = parse_expr(question)
            sol = simplify(expr)
        return str(sol)
    except Exception as e:
        return f"Could not solve: {str(e)}"
