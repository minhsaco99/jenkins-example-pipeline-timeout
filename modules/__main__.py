from .test import HelloWorld
import sys

md = HelloWorld()
if len(sys.argv) > 1:
    md.print_with_variable(sys.argv[1])