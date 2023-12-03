def greet(name: str) -> str:
    return name

# Mypy type checking
result: str = greet(42)

if __name__ == '__main__':
    print(result)
