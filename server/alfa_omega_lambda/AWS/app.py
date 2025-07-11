import json
import requests
from controllers.math_controller import calculate as math_calculate

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logsd
        print(e)

        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world, this has all be done through git actions and big brain",
            "location": ip.text.replace("\n", "")
        }),
    }

def calculate(event, context):
    try:
        body = event.get("body")
        if body:
            data = json.loads(body)
            expression = data.get("expression")
            if expression is not None:
                result = math_calculate(expression)
                return {
                    "statusCode": 200,
                    "body": json.dumps(result)
                }
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing 'expression' in request body"})
        }
    except Exception as e:
        print(f"Error calculating expression: {e}")
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }