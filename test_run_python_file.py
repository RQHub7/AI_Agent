from functions.run_python_file import run_python_file

def test():
    print("Calculator usage instructions:")
    print(run_python_file("calculator", "main.py"))
    print()
    print("Calculator run test... apparently nasty rendered result:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print()
    print("Runs for each calculator test in tests.py:")
    print(run_python_file("calculator", "tests.py"))
    print()
    print("Error expected:")
    print(run_python_file("calculator", "../main.py"))
    print()
    print("Error expected:")
    print(run_python_file("calculator", "nonexistent.py"))
    print()
    print("Error expected:")
    print(run_python_file("calculator", "lorem.txt"))
    print()

if __name__ == "__main__":
    test()