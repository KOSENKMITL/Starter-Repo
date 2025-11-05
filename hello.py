# Edit your name below, then run the file or tests.
# Expected output: Hello, <YourName>!

NAME = "REPLACE_WITH_YOUR_NAME"

def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet(NAME))
