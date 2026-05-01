from functions.get_file_content import get_file_content

def test():
    print("Contents of main.py:")
    print(get_file_content("calculator", "main.py"))
    print()
    print("Contents of pkg/calculator.py:")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()
    print("Contents of /bin/cat.py:")
    print(get_file_content("calculator", "/bin/cat.py"))
    print()
    print("Contents of pkg/does_not_exist.py:")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print()

if __name__ == "__main__":
    test()