import sys

def fibonacci_generator():
    """A generator for Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    try:
        # Get the number of Fibonacci terms to generate from the command line
        n = int(input("Enter the number of Fibonacci numbers to generate: "))

        if n <= 0:
            print("Please enter a positive integer.")
            return

        # Create an instance of the generator
        fib_gen = fibonacci_generator()

        print(f"The first {n} Fibonacci numbers are:")
        for _ in range(n):
            print(next(fib_gen))

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
