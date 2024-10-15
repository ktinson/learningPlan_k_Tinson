def main():
    name =input("Enter name: ")
    hello(name)
    squared(3)
def squared(n):
    return n * n
def hello(to):
    print(f'Hello,', to)
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    z = x + y
    print(squared(x), squared(y))
    print(z)
main()
