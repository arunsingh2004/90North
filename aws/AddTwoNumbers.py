def lambda_handler(event, context):
    num1 = event.get('num1')
    num2 = event.get('num2')
    return {'result': num1 + num2}
