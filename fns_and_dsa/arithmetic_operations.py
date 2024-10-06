def perform_operation(num1, num2, operation):
    result = 0.0
    match(operation):
        case 'add':
            result=num1+num2
        case 'subtract':
            result=num1-num2
        case 'multiply':
            result=num1*num2
        case 'divide':
            if num1 != 0:
                result=num1*num2
            else:
                print("cant divide by zero")
                return 
    return result
