import sys

class HelloWorld:
    def __init__(self) -> None:
        print('Hello World from HelloWorld')

    def print_with_variable(self, variable):
        print(f"Hello {variable} from HelloWorld")
test = HelloWorld()

if len(sys.argv) > 1:
    test.print_with_variable(sys.argv[1])