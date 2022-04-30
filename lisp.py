import enum
import math
import re

TYPE = enum.Enum(
    'TYPE', 'NIL FUNCTION ATOM STRUCTURE ARRAY SEQUENCE SYMBOL NUMBER LIST STRING INTEGER RATIO FLOAT')

class LispObject:
    """ Standard Lisp object for all types """
    type = None
    value = None
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __str__(self):
        return self.value
    def __repr__(self):
        return str(self.value)

class LispException(Exception):
    """ Lisp Exception """
    message = "LispException: "
    def __init__(self, message):
        self.message += message
    def __str__(self):
        return self.message
    def __repr__(self):
        return self.message

class NIL(LispObject):
    """ Nil object extends LispObject """
    def __init__(self):
        super().__init__(TYPE.NIL, 'NIL')

def OUT(string, lisp_string=None):
    """ Prints string to stdout and to file """
    print(string)
    try:
        if lisp_string:
            OUT_FILE.write("> " + lisp_string + '\n')
        OUT_FILE.write(string + '\n')
    except:
        pass

def float_to_int(x):
    """ Converts float to int if possible """
    if x == int(x):
        return int(x)
    return x

def ADD(args):
    """ Adds all arguments together """
    if len(args) < 2:
        raise LispException("Not enough arguments")
    return float_to_int(sum(args))

def SUBTRACT(args):
    """ Subtracts all arguments from first argument """
    if len(args) < 2:
        raise LispException("Not enough arguments")
    for i in range(1, len(args)):
        args[0] = args[0] - args[i]
    return float_to_int(args[0])

def DIVIDE(args):
    """ Divides first argument by all other arguments """
    if len(args) < 2:
        raise LispException("Not enough arguments")
    for arg in args:
        if arg == 0:
            return ["ERROR divided by zero"]
    for i in range(1, len(args)):
        args[0] = args[0] / args[i]
    return float_to_int(args[0])

def MULTIPLY(args):
    """ Multiplies all arguments together """
    if len(args) < 2:
        raise LispException("Not enough arguments")
    for i in range(1, len(args)):
        args[0] = args[0] * args[i]
    return float_to_int(args[0])

def LT(args):
    """ Less than: returns true if first argument is less than second """
    if len(args) < 2:
        raise LispException("Not enough arguments")
    if len(args) > 2:
        raise LispException("Too many arguments")
    if args[0] < args[1]:
        return True
    else:
        return False

def GT(args):
    """ Greater than: returns true if first argument is greater than second """
    if len(args) < 2:
        raise LispException("Not enough arguments")
    if len(args) > 2:
        raise LispException("Too many arguments")
    if args[0] > args[1]:
        return True
    else:
        return False

def LE(args):
    """ Less than or equal: returns true if first argument is less than or equal to second """
    if len(args) < 2:
        raise LispException("Not enough arguments")
    if len(args) > 2:
        raise LispException("Too many arguments")
    if args[0] <= args[1]:
        return True
    else:
        return False
def GE(args):
    """ Greater than or equal: returns true if first argument is greater than or equal to second """
    if len(args) < 2:
        raise LispException("Not enough arguments")
    if len(args) > 2:
        raise LispException("Too many arguments")
    if args[0] >= args[1]:
        return True
    else:
        return False

def IF(args):
    """ If statement: if first argument is true, evaluates second argument, else evaluates third """
    if len(args) < 3:
        raise LispException("Not enough arguments")
    if len(args) > 3:
        raise LispException("Too many arguments")
    if evaluate(args[0]) == True:
        return evaluate(args[1])
    else:
        return evaluate(args[2])

def CAR(args):
    """ Returns first element of list """
    if len(args) != 1:
        raise LispException("Not enough arguments")
    if type(args[0]) != list:
        raise LispException("Argument is not a list")
    if len(args[0]) == 0:
        raise LispException("List is empty")
    return args[0][0]

def CDR(args):
    """ Returns all but first element of list """
    if len(args) != 1:
        raise LispException("Not enough arguments")
    if type(args[0]) != list:
        raise LispException("Argument is not a list")
    if len(args[0]) == 0:
        raise LispException("List is empty")
    return args[0][1:]

def DEFINE(args):
    """ Defines a variable: first argument is name, second is value """
    if len(args) != 2:
        raise LispException("Not enough arguments")
    if type(args[0]) != str:
        print(args[0])
        raise LispException("First argument is not a string")
    VARS[args[0]] = args[1]
    return args[1]

def DEFUN(args):
    """ Defines a function: first argument is name, second is list of arguments, third is body """
    if len(args) < 3:
        raise LispException("Not enough arguments")
    if type(args[0]) != str:
        raise LispException("First argument is not a string")
    if type(args[1]) != list:
        raise LispException("Second argument is not a list")
    FUNCTIONS[args[0]] = args[1], args[2]
    return args[0]

def AND(args):
    """ Returns true if all arguments are true """
    if len(args) < 2:
        raise LispException("Not enough arguments")
    for arg in args:
        if arg != True:
            return False
    return True

def OR(args):
    """ Returns true if any argument is true """
    if len(args) < 2:
        raise LispException("Not enough arguments")
    for arg in args:
        if arg == True:
            return True
    return False

def EQ(args):
    """ Returns true if arguments are equal """
    if len(args) < 2:
        raise LispException("Not enough arguments")
    if len(args) > 2:
        raise LispException("Too many arguments")
    return args[0] == args[1]

def NEQ(args):
    """ Returns true if arguments are not equal """
    if len(args) < 2:
        raise LispException("Not enough arguments")
    if len(args) > 2:
        raise LispException("Too many arguments")
    return args[0] != args[1]

def NOT(args):
    """ Returns true if argument is false """
    if len(args) != 1:
        raise LispException("Not enough arguments")
    if args[0] == True:
        return False
    else:
        return True

def WRITE(args):
    """ Writes all arguments to stdout separated by spaces """
    if len(args) < 1:
        raise LispException("Not enough arguments")
    string = ""
    for arg in args:
        string += str(arg) + " "
    print(string)

def SQRT(args):
    """ Returns square root of argument """
    if len(args) != 1:
        raise LispException("Not enough arguments")
    if type(args[0]) != int and type(args[0]) != float:
        raise LispException("Argument is not a number")
    return float_to_int(math.sqrt(args[0]))

def POW(args):
    """ Returns first argument raised to the power of second argument """
    if len(args) != 2:
        raise LispException("Not enough arguments")
    if type(args[0]) != int and type(args[0]) != float:
        raise LispException("First argument is not a number")
    if type(args[1]) != int and type(args[1]) != float:
        raise LispException("Second argument is not a number")
    return float_to_int(math.pow(args[0], args[1]))

def CONS(args):
    """ Returns list with first argument as first element and second argument as rest of list """
    if len(args) != 2:
        raise LispException("Not enough arguments")
    result = [args[0]]
    for arg in args[1]:
        result.append(arg)
    return result

def QUIT():
    """ Exits program """
    OUT('Bye.')
    OUT_FILE.close()
    exit()

def reset():
    """ Resets all variables to their default values """
    global VARS, FUNCTIONS
    VARS = O_VARS
    FUNCTIONS = {}

VARS = {}   # Global variables
FUNCTIONS = {}  # Global functions
O_VARS = {'TRUE': True, 'FALSE': False, 'NIL': None, 'T': True, 'F': False, 'NIL': NIL(), 'VARS': VARS} # Original variables used to reset
OUT_FILE = 'lisp.out'   # Output file

def get_tokens(string):
    """ Returns list of tokens from string recursively """
    if string == '':
        return []
    tokens = re.findall(r'\(|\)|"[^"]+"|\'|[^\s\(\)]+', string) # Find all tokens in string
    par_count = 0
    split_string = []
    temp = []
    skip_cycle = False
    # find all single-quotes and move it to the inside of its respective list
    for i in range(len(tokens)):
        if tokens[i] == "'" and tokens[i + 1] == '(' and not skip_cycle:
            tokens[i] = tokens[i + 1]
            tokens[i + 1] = "'"
            skip_cycle = True   # skip next cycle to avoid a quote two times around and index out of range
        else:
            skip_cycle = False

    # split ciomplete lists into separate lists
    for token in tokens:
        temp.append(token)
        if token == '(':
            par_count += 1
        elif token == ')':
            par_count -= 1
        if par_count == 0:
            split_string.append(temp)
            temp = []
    def recur(index):
        """ Recursively finds parentheses and creates nested lists """
        try:
            result = []
            token = tokens[index]
            while token != ")":
                if token == "(":
                    r_tokens, index = recur(index + 1)
                    result.append(r_tokens)
                else:
                    result.append(token)
                index += 1
                token = tokens[index]
                
            return result, index
        except IndexError:
            raise LispException("Mismatched parentheses")
    temp = []
    # if a single token is found without parentheses, append it to the list as its own command
    for i in range(len(split_string)):
        if '(' not in split_string[i] and ')' not in split_string[i]:
            temp.append(split_string[i])
            del split_string[i]
    # convert the lists of tokens into nested lists based on parentheses
    for s in split_string:
        tokens = s
        temp.append(recur(1)[0])
    return temp

def parenthesize(tokens):
    """ Parenthesize tokens: prepend "(" and append ")" to tokens if they are not already parenthesized. Makes output more readable """
    result = ""
    if type(tokens) != list:
        return str(tokens)
    for i in range(len(tokens)):
        # add spaces between tokens
        if i != 0:
            result += " "
        if type(tokens[i]) == list:
            result += "(" + parenthesize(tokens[i]) + ")"
        else:
            result += str(tokens[i])
    return result

def convert_numbers(tokens):
    """ Converts all numbers in tokens to integers or floats if possible """
    for i in range(len(tokens)):
        if type(tokens[i]) == list:
            tokens[i] = convert_numbers(tokens[i])
        if type(tokens[i]) == str:
            try:
                tokens[i] = int(tokens[i])
            except ValueError:
                try:
                    tokens[i] = float(tokens[i])
                except ValueError:
                    pass
    return tokens

def evaluate(tokens, scope=None):
    """ Evaluates tokens recursively starting from inside out """
    tokens = convert_numbers(tokens)    # convert all string numbers to integers or floats if possible
    if len(tokens) == 0:    # if no tokens are found, return NIL
        return NIL()
    if not scope:   # if no scope is given, use global scope [unimplemented and not used]
        global VARS
    else:
        VARS = scope.variables
    if tokens[0] == "'":    # if first token is a quote, return the rest of the list unevaluated
        return tokens[1:]
    if type(tokens[0]) == str and VARS.get(tokens[0]) is not None:  # if first token is a variable, return its value
        return VARS[tokens[0]]

    if tokens[0] in FUNCTIONS:  # if first token is a function, evaluate it
        vars = list(FUNCTIONS[tokens[0]][0])    # get variables from function
        prototype = list(FUNCTIONS[tokens[0]][1])   # get prototype from function
        if (len(tokens[1:])) != len(vars):  # if number of arguments is not equal to number of variables, raise exception
            raise LispException("Wrong number of arguments")
        else:
            values = {}   # create dictionary to store values
            for i in range(len(vars)):  # for each variable in the call, store its value in the dictionary
                values[vars[i]] = tokens[i + 1]
            def recur(prototype, values):   # recursively replace variables in the prototype with the values in the dictionary
                for i in range(len(prototype)): # for each token in the prototype
                    if type(prototype[i]) == list:  # if token is a list, recursively call recur
                        prototype[i] = recur(prototype[i], values)
                    for k in values:    # replace all variables in the prototype with their values
                        if k == prototype[i]:   # if token is a variable, replace it with its value
                            prototype[i] = values[k]
                        
                return prototype
            tokens = recur(prototype, values)   # replace all variables in the prototype with their values then continue evaluating
    

    skip_cycles = 0  # skip cycles to avoid unwanted evaluations
    for i in range(len(tokens)):    # for each token
        if skip_cycles > 0:
            skip_cycles -= 1
            continue
        if tokens[i] == 'DEFUN':    # if token is DEFUN do not evaluate it or its arguments
            skip_cycles = 3
            continue
        if tokens[i] == 'IF':   # if token is IF do not evaluate it or its arguments
            skip_cycles = 3
            continue
        if type(tokens[i]) == str and tokens[i] in FUNCTIONS:   # if token is a function, do not evaluate it or its arguments
            skip_cycles = len(FUNCTIONS[tokens[i]][0])
            continue
        if type(tokens[i]) == list:   # if token is a list, evaluate it to expand it and get its value
            tokens[i] = evaluate(tokens[i])
        if type(tokens[i]) == str and VARS.get(tokens[i]) is not None and tokens[0] != "DEFINE" and tokens[0] != "SET!":    # if token is a variable and it is not a define or set!, replace it with its value
            tokens[i] = VARS[tokens[i]]

    tokens = [x for x in tokens if x != "'"]    # remove all leftover single quotes

    if tokens[0] == '+':    # if first token is +, add all numbers in the list
        return ADD(tokens[1:])
    elif tokens[0] == '-':  # if first token is -, subtract all numbers in the list
        return SUBTRACT(tokens[1:])
    elif tokens[0] == '/':  # if first token is /, divide all numbers in the list
        return DIVIDE(tokens[1:])
    elif tokens[0] == '*':  # if first token is *, multiply all numbers in the list
        return MULTIPLY(tokens[1:])
    elif tokens[0] == '<':  # if first token is <, return whether all numbers in the list are less than the next number
        return LT(tokens[1:])
    elif tokens[0] == '>':  # if first token is >, return whether all numbers in the list are greater than the next number
        return GT(tokens[1:])
    elif tokens[0] == '<=':  # if first token is <=, return whether all numbers in the list are less than or equal to the next number
        return LE(tokens[1:])
    elif tokens[0] == '>=':  # if first token is >=, return whether all numbers in the list are greater than or equal to the next number
        return GE(tokens[1:])
    elif tokens[0] == 'IF': # if first token is IF, evaluate the first argument and return the second argument if it is true, otherwise return the third argument
        return IF(tokens[1:])
    elif tokens[0] == 'CDR':    # if first token is CDR, return the rest of the list
        return CDR(tokens[1:])
    elif tokens[0] == 'CAR':    # if first token is CAR, return the first element of the list
        return CAR(tokens[1:])
    elif tokens[0] == 'CONS':   # if first token is CONS, return a list with the first argument as the first element and the rest of the list as the rest of the list
        return CONS(tokens[1:])
    elif tokens[0] == 'OR':    # if first token is OR, return whether any of the arguments are true
        return OR(tokens[1:])
    elif tokens[0] == 'AND':    # if first token is AND, return whether all of the arguments are true
        return AND(tokens[1:])
    elif tokens[0] == '=':  # if first token is =, return whether all values in the list are equal
        return EQ(tokens[1:])
    elif tokens[0] == '!=':  # if first token is !=, return whether all values in the list are not equal
        return NEQ(tokens[1:])
    elif tokens[0] == 'NOT':    # if first token is NOT, return whether the argument is false
        return NOT(tokens[1:])
    elif tokens[0] == 'WRITE':  # if first token is WRITE, print all arguments
        return WRITE(tokens[1:])
    elif tokens[0] == 'EXIT' or tokens[0] == 'QUIT':    # if first token is EXIT or QUIT, exit the program
        QUIT()
    elif tokens[0] == 'DEFINE':   # if first token is DEFINE, define a variable with the first argument as the name and the second argument as the value
        return DEFINE(tokens[1:])
    elif tokens[0] == 'DEFUN':  # if first token is DEFUN, define a function with the first argument as the name and the second argument as the list of variables and the third argument as definition
        return DEFUN(tokens[1:])
    elif tokens[0] == 'SQRT':   # if first token is SQRT, return the square root of the argument
        return SQRT(tokens[1:])
    elif tokens[0] == 'POW':    # if first token is POW, return the first argument to the power of the second argument
        return POW(tokens[1:])
    elif tokens[0] == 'SET!':   # if first token is SET!, set the value of the first argument to the second argument
        return DEFINE(tokens[1:])
    elif tokens[0] == True:  # if first token is True, return T
        return 'T'
    elif tokens[0] == False: # if first token is False, return NIL
        return NIL()
    else:   # if first token is not a function, return an error
        return f"{tokens[0]} is not a function name; try using a symbol instead"

def interpret(lisp_string):
    """ Interpret a lisp string and return the result """
    if lisp_string == ")":  # if lisp string is ), return an error
        return 'An object cannot start with \')\''
    lisp_string = re.sub(r'\b(?<!")(\w+)(?!")\b', lambda match: match.group(1).upper(), lisp_string)    # convert all words to uppercase
    tokens = get_tokens(lisp_string)    # convert lisp string to lists of lists of tokens
    for i in range(len(tokens)):    # for each lisp command evaluate it
        if type(tokens[i]) == list:
            tokens[i] = evaluate(tokens[i])
            out = [tokens[i]]   # save the last output
    out = parenthesize(out)   # parenthesize the output
    return out  # return the output

def main():
    reset()
    try:    # open output file
        global OUT_FILE
        OUT_FILE = open(OUT_FILE, 'w+')
    except FileNotFoundError:
        print("File not found")


    try:
        while True:   # loop until user quits
            lisp_string = input("> ")
            level = 0
            for char in lisp_string:
                if char == '(':
                    level += 1
                elif char == ')':
                    level -= 1
            while level > 0:
                lisp_string_cont = input()
                for char in lisp_string_cont:
                    if char == '(':
                        level += 1
                    elif char == ')':
                        level -= 1
                lisp_string += lisp_string_cont
            OUT(interpret(lisp_string), lisp_string=lisp_string)
    except LispException as e:
        print(e)
    except KeyboardInterrupt:
        print("(exit)")
        try:
            OUT_FILE.close()
        except:
            pass
        QUIT()

if __name__ == '__main__':
    main()