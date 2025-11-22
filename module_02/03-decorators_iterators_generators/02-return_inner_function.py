
def calculator(operation):
    def addition(a, b):
        return (a + b)
    
    def subtraction(a, b):
        return (a - b)
        
    def multiplication(a, b):
        return (a * b)
        
    def division(a, b):
        return (a / b)
    
    match operation:
        case '+':
            return addition
        case '-':
            return subtraction
        case '*':
            return multiplication
        case '/':
            return division
        

op = calculator('+')(2, 2)
print(op)
# 4
op = calculator('-')
print(op(2, 2))
# 0
op = calculator('*')
print(op(2, 2))
# 4
op = calculator('/')
print(op(2, 2))
# 1.0

