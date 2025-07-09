


def calculate(request):
    """
    Calculate the result of a mathematical expression.
    """
    expression = request.get_json().get('expression', '')
    
    if not expression:
        return {'error': 'No expression provided'}, 400
    
    try:
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, {})
        return {'result': result}
    except Exception as e:
        return {'error': str(e)}, 400