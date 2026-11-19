print("\n-----------------WELCOME TO THE GAME-----------------")
def game():
    while True:
        print("\nEnter 1 for the factorial of a number")
        print("Enter 2 for the sum of natural numbers")
        print("Enter 3 for a BMI calculation")
        print("Enter 4 for the fibonacci series")
        print("Enter 5 for an ATM use case")
        print("Enter Q to quit the game")
        n = input()
        if n == '1':
            def factorial(x):
                """Factorial of a number"""
                if x == 0 or x == 1:
                    return 1
                elif x < 0:
                    return "No negative values only positive numbers to be accepted"
                else:
                    return x*factorial(x-1)
            n = int(input("Enter a value:"))
            print(factorial(n))
        elif n == '2':
            def sum_of_natural(x):
                """Sum of Natural numbers"""
                if x == 0 or x == 1:
                    return 1
                elif x<0:
                    return "No negative values only positive numbers to be accepted"
                else:
                    return x+sum_of_natural(x-1)
            n = int(input("Enter a value:"))
            print(sum_of_natural(n))
        elif n == '3':
            def calculate_bmi(n):
                """BMI Calculation"""
                if n <= 0:
                    return
                for i in range(n):
                    name = input("Enter the name: ")
                    weight = float(input("Enter the weight in Kgs: "))
                    height = float(input("Enter the height in meters: "))
                    if weight > 0 and height > 0:
                        bmi = weight / (height**2)
                        if bmi < 18.5:
                            print(f"{name} --> You are underweight as BMI is {bmi:.2f}")
                        elif 18.5 <= bmi <= 24.9:
                            print(f"{name} --> You are in perfect physique, BMI is {bmi:.2f}")
                        elif 25 <= bmi <= 29.9:
                            print(f"{name} --> You are in over weight need to maintain diet, BMI is {bmi:.2f}")
                        else:
                            print(f"{name} --> Obesity, BMI is {bmi:.2f}")
                    else:
                        print("Enter only +ve values")
            total_users = int(input("How many users: "))
            calculate_bmi(total_users)
        elif n == '4':
            def fibonacci(n):
                """Fibonacci series"""
                if n <= 0:
                    return 0
                elif n == 1:
                    return 1
                else:
                    return fibonacci(n-1)+fibonacci(n-2)
            number = int(input("Enter a value:"))
            for i in range(number):
                print(fibonacci(i),end=" ")
            print()
        elif n == '5':
            balance = 5000
            def atm():
                """ATM Usecase"""
                nonlocal balance
                print("\n===== ATM MENU =====")
                while True:
                    print("\n1. Check Balance")
                    print("2. Withdraw")
                    print("3. Deposit")
                    print("4. Exit")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        print("Your Current Balance is:", balance)
                    elif choice == 2:
                        amount = int(input("Enter withdrawal amount: "))
                        if amount <= 0:
                            print("Enter a valid amount")
                        elif amount > balance:
                            print("Insufficient Balance")
                        else:
                            balance -= amount
                            print("Withdrawal Successful!")
                    elif choice == 3:
                        amount = int(input("Enter deposit amount: "))
                        if amount <= 0:
                            print("Enter a valid amount")
                        else:
                            balance += amount
                            print("Deposit Successful!")
                    elif choice == 4:
                        print("Thank you for using ATM!")
                        break
                    else:
                        print("Invalid Choice!")
            atm()
        elif n == 'Q':
            break
        else:
            print("Enter only numbers from 1 to 5")
game()
    
