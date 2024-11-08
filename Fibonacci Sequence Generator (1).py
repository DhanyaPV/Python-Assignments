def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    n = int(input("Enter the number of terms: "))
    fib_sequence = fibonacci(n)
    print(f"Fibonacci sequence up to {n} terms: {', '.join(map(str, fib_sequence))}")

if __name__ == "__main__":
    main()
