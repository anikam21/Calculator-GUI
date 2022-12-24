class CalculatorFunctions:
    def __init__(self, number1, number2, operation):
        self.number1 = number1
        self.number2 = number2
        self.operation = operation

    def addtion(self):
        """Returns an addtion of two number"""
        addition  = self.number1 + self.number2
        return print(addition)

    def subtraction(self):
        """Returns the subtraction of two number"""
        subtraction = self.number1 - self.number2
        return print("Subtraction", subtraction) 
    
    def multiplication(self):
        """Returns the multiplication of two number"""
        multiplication = self.number1*self.number2
        return print("Multiplication", multiplication)
    
    def division(self):
        """Returns the division of two number"""
        division = self.number1/self.number2
        return print("Division", division) 

    def choose_operation(self):
        """Allows the user to choose an operation"""
        if self.operation == '+' :
            self.addtion()
        elif self.operation == '-':
            self.subtraction()
        elif self.operation == '*':
            self.multiplication()
        elif self.operation == '/':
            self.division()
        else:
            print('Error. Please choose one of the listed operators')


while True:  
    first_number = int(input('Choose a number: '))
    second_number = int(input('Choose a second number: '))
    operation = input('Enter the operand +, -, *, / ')
    calc_obj = CalculatorFunctions(first_number, second_number, operation)
    
    result = calc_obj.choose_operation()

    user_cont = input('Would you like to continue? (y/n) ')
    if user_cont == 'y':
        continue
    else: 
        break
