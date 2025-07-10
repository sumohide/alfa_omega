


def calculate(expression):
    """
    Calculate the result of a mathematical expression.
    """
    print(f"Received expression: {expression}")
    if not expression:
        return {'error': 'No expression provided'}, 400
    
    try:
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, {})
        return {'result': result}
    except Exception as e:
        return {'error': str(e)}, 400