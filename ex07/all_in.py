import sys

def search_capital_or_state(expressions):
    states = {'oregon': 'Salem', 'nova jersey': 'Trenton'}
    capitals = {'trenton': 'Nova Jersey', 'salem': 'Oregon'}

    if not expressions or len(expressions) != 1:
        return

    results = []
    for expression in expressions[0].split(','):
        expr = expression.strip().lower()
        if expr == '':
            continue
        if expr in states:
            results.append(f"{states[expr].title()} is the capital of {expr.title()}")
        elif expr in capitals:
            results.append(f"{capitals[expr].title()} is the capital of the state {expr.title()}")
        else:
            results.append(f"{expression.strip()} is neither a capital nor a state")

    print("\n".join(results))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        search_capital_or_state(sys.argv[1:])
