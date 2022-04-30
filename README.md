# Welcome to my Lisp Interpreter!
This is a lisp interpeter that is written entirely in python. It is a very simple interpreter that can be used to evaluate lisp expressions. It is written in such a way that it can be used as a library for other projects by simply importing the interpreter.

## Testing
For ease of testing, a test script has been included \`test.py\`. This will run the commands as specified in the file on canvas and verify correct output and behavior.
```
python3 test.py
```

## Running
### Note: A Python 3 interpreter is required to run this interpreter.
To run the interpreter, use the following command:
```
python3 lisp.py
```

## Syntax
Uses standard lisp syntax. Can handle multiple expressions on a single line.

## Features
- Evaluates lisp expressions
- Supports basic arithmetic
- Supports basic boolean logic
- Supports basic comparison
- Supports basic list operations
- Supports variable declaration and referencing
- Supports function declaration and calling
- Supports adcanced arithmetic such as exponentiation
- Support for recursive functions is planned


## Built-in Functions
- \`write\`: prints the given expression to the console
- '+': adds arguments together
- '-': subtracts all arguments from the first argument
- '*': multiplies all arguments together
- '/': divides all arguments from the first argument
- 'if': evaluates the first argument and evaluates the second if it is true, otherwise evaluates the third
- '=': compares the first argument to the second argument and returns true if they are equal
- '<': compares the first argument to the second argument and returns true if the first is less than the second
- '>': compares the first argument to the second argument and returns true if the first is greater than the second
- '<=': compares the first argument to the second argument and returns true if the first is less than or equal to the second
- '>=': compares the first argument to the second argument and returns true if the first is greater than or equal to the second
- 'not': returns the opposite of the argument
- ': returns the second argument
- 'car': returns the first element of the argument
- 'cdr': returns all elements of the argument except the first
- 'cons': returns a list with the first argument as the first element and the second argument as the second element
- 'defun': defines a function with the given name and arguments
- 'define' or 'defvar': defines a variable with the given name and value
- 'and': returns true if all arguments are true
- 'or': returns true if any argument is true
- 'pow': returns the first argument to the power of the second argument
- 'sqrt': returns the square root of the argument
- 'exit' or 'quit': exits the interpreter

## Known Bugs
- Recursive functions are broken and will not work when called