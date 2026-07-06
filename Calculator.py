# calculadora

while True:
 
 print('\nWelcome to the calculator!\n')

 num1 = input('\nChoose the first number: ')

 while not num1.isdigit():
     print('\nInvalid input. Please enter a valid number.\n')
     num1 = input('\nChoose the first number: ')

 num1 = float(num1)


 num2 = input('\nChoose the second number: ')

 while not num2.isdigit():
     print('\nInvalid input. Please enter a valid number.\n')
     num2 = input('\nChoose the second number: ')

 num2 = float(num2)

 operation = input('\nChoose the operation (+, -, *, /): ')

 while operation not in ['+', '-', '*', '/']:
     print('\nInvalid operation. Please enter a valid operation (+, -, *, /).\n')
     operation = input('Choose the operation (+, -, *, /): ')


 if operation == '+':
     res = num1 + num2
     print(f'\nThe result of the addition is: {res}\n')
 elif operation == '-':
     res = num1 - num2
     print(f'\nThe result of the subtraction is: {res}\n')
 elif operation == '*':
     res = num1 * num2
     print(f'\nThe result of the multiplication is: {res}\n')
 elif operation == '/':
     if num2 != 0:
         res = num1 / num2
         print(f'\nThe result of the division is: {res}\n')
     else:
         print('\nError: Division by zero is not allowed.')

         while num2 == 0:
             num2 = float(input('\nChoose a non-zero number for the second operand: '))

         res = num1 / num2
         print(f'\nThe result of the division is: {res}\n')


 answer = input('\nDo you want to perform another calculation? (yes/no): ')

 if answer.lower() == 'no':
     print('\nThank you for using the calculator. Goodbye!\n')
     break
