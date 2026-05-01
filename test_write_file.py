from functions.write_file import write_file

def test():
    print("Calculator subdir write test:")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print()
    print("Calculator/pkg subdir write test:")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print()
    print("Temporary new subdir write test:")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print()

if __name__ == "__main__":
    test()