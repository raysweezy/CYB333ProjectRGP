# main.py

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python main.py [raymond]")
    else:
        name = sys.argv[1]
        print(greet(name))