# Factorial Calculator in Python

def factorial(n):
    # Base case: 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial(n - 1)
        return n * factorial(n - 1)

def main():
    print("=======================================")
    print("         FACTORIAL CALCULATOR          ")
    print("=======================================")
    
    # Input from user
    num = int(input("Enter a number: "))

    print("\n---------------------------------------")

    if num < 0:
        print(" Error: Factorial of a negative number doesn't exist.")
    else:
        print(f" Factorial of {num} is: {factorial(num)}")
    
    print("---------------------------------------")
    print("          Thank you for using          ")
    print("     the Factorial Calculator!         ")
    print("=======================================")

if __name__ == "__main__":
    main()
