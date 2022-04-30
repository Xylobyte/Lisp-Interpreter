# Test Block lisp interpreter with assert statements
import lisp

INTERPRET = lisp.interpret

def RESET():
    lisp.reset() # import lisp

ERRORS = 0
TESTS = 20

try:
    assert INTERPRET("(define m (define r 10))") == '10'
    assert INTERPRET("r") == '10'
    assert INTERPRET("m") == '10'
except Exception as e:
    print(f"Test Block 1:\t\033[91mFAILED\033[0m")
    print("Got output:", INTERPRET("(define m (define r 10))"))
    ERRORS += 1
else:
    print(f"Test Block 1:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("()") == 'NIL'
    assert INTERPRET(")") == 'An object cannot start with \')\''
    assert INTERPRET("(2)") == '2 is not a function name; try using a symbol instead'
except Exception as e:
    print(f"Test Block 2:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 2:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("'(2)") == '(2)'
except Exception as e:
    print(f"Test Block 3:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 3:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("'(+ 1 2)") == '(+ 1 2)'
except Exception as e:
    print(f"Test Block 4:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    # "PASSED" in green
    print(f"Test Block 4:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("'(+ a b)") == '(+ A B)'
except Exception as e:
    print(f"Test Block 5:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 5:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(if (> 10 20) (+ 1 1) (+ 3 3))") == '6'
    assert INTERPRET("(if (< 10 20) (+ 1 1) (+ 3 3))") == '2'
    assert INTERPRET("(if (and (> 10 20) T) (+ 1 1) (+ 3 3))") == '6'
    assert INTERPRET("(if (or (> 10 20) T) (+ 1 1) (+ 3 3))") == '2'
    assert INTERPRET("(if (and (> 20 10) NIL) (+ 1 1) (+ 3 3))") == '6'
    assert INTERPRET("(if (and (= 10 10) (!= 10 10)) (+ 1 1) (+ 3 3))") == '6'
    assert INTERPRET("(if (or (= 10 10) (!= 10 10)) (+ 1 1) (+ 3 3))") == '2'
except Exception as e:
    print(f"Test Block 6:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 6:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(define a 10)") == '10'
    assert INTERPRET("(define b 20)") == '20'
    assert INTERPRET("(if (> a b) (+ 1 1) (+ 3 3))") == '6'
    assert INTERPRET("(if (< a b) (+ 1 1) (+ 3 3))") == '2'
    assert INTERPRET("(if (and (> a b) T) (+ 1 1) (+ 3 3))") == '6'
    assert INTERPRET("(if (or (> a b) T) (+ 1 1) (+ 3 3))") == '2'
    assert INTERPRET("(if (and (= a a) (!= a a)) (+ 1 1) (+ 3 3))") == '6'
    assert INTERPRET("(if (or (= a a) (!= a a)) (+ 1 1) (+ 3 3))") == '2'
    assert INTERPRET("(if (not T) (+ 1 1) (+ 3 3))") == '6'
    assert INTERPRET("(if (not NIL) (+ 1 1) (+ 3 3))") == '2'
except Exception as e:
    print(f"Test Block 7:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 7:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(define a 3)") == '3'
    assert INTERPRET("(define b 2)") == '2'
    assert INTERPRET("(if (< a b) (+ 1 1) (+ 3 3))") == '6'
    assert INTERPRET("(if (> a b) (+ 1 1) (+ 3 3))") == '2'
except Exception as e:
    print(f"Test Block 8:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 8:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(define a 3)") == '3'
    assert INTERPRET("(define b 2)") == '2'
    assert INTERPRET("(define x 2)") == '2'
    assert INTERPRET("(define y 2)") == '2'
    assert INTERPRET("(if (< a b) (+ x y) (- x y))") == '0'
    assert INTERPRET("(if (> a b) (+ x y) (- x y))") == '4'
except Exception as e:
    print(f"Test Block 9:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 9:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(sqrt 4)") == '2'
    assert INTERPRET("(sqrt (+ 2 2))") == '2'
    assert INTERPRET("(pow 2 3)") == '8'
    assert INTERPRET("(pow (+ 1 1) (- 4 1))") == '8'
except Exception as e:
    print(f"Test Block 10:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 10:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(define x 2)") == '2'
    assert '1.4142135' in INTERPRET("(sqrt x)")
except Exception as e:
    print(f"Test Block 11:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 11:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(define r 10)") == '10'
    assert INTERPRET("(set! r 5)") == '5'
    assert INTERPRET("r") == '5'
    assert INTERPRET("(set! r (* 2 2))") == '4'
    assert INTERPRET("r") == '4'
    assert INTERPRET("(set! r (* r r))") == '16'
    assert INTERPRET("r") == '16'
    assert INTERPRET("(set! r 2)") == '2'
except Exception as e:
    print(f"Test Block 12:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 12:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(+ 2 3)") == '5'
    assert INTERPRET("(- 3 2)") == '1'
    assert INTERPRET("(* 2 3)") == '6'
    assert INTERPRET("(/ 6 2)") == '3'
    assert INTERPRET("(/ 6 0)") == '(ERROR divided by zero)'
except Exception as e:
    print(f"Test Block 13:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 13:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(+ (+ 2 3) 5)") == '10'
    assert INTERPRET("(- (- 2 3) 5)") == '-6'
    assert INTERPRET("(* (* 2 3) 5)") == '30'
except Exception as e:
    print(f"Test Block 14:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 14:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(define a 5)") == '5'
    assert INTERPRET("(define b 10)") == '10'
    assert INTERPRET("(+ a b)") == '15'
    assert INTERPRET("(- b a)") == '5'
    assert INTERPRET("(* a b)") == '50'
    assert INTERPRET("(/ b a)") == '2'
except Exception as e:
    print(f"Test Block 15:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 15:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(define x 2)") == '2'
    assert INTERPRET("(define y 4)") == '4'
    assert INTERPRET("(define z 8)") == '8'
    assert INTERPRET("(+ (+ x y) z)") == '14'
    assert INTERPRET("(* (* x y) z)") == '64'
    assert INTERPRET("(- (- x y) z)") == '-10'
except Exception as e:
    print(f"Test Block 16:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 16:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(defun ADD (x y) (+ x y)) (ADD 8 3)") == '11'
    assert INTERPRET("(defun SUB (x y) (- x y)) (SUB 3 2)") == '1'
    assert INTERPRET("(defun MUL (x y) (* x y)) (MUL 2 3)") == '6'
    assert INTERPRET("(defun DIV (x y) (/ x y)) (DIV 6 2)") == '3'
    assert INTERPRET("(defun ADD2 (x y z) (+ (+ x y) z)) (ADD2 2 2 2)") == '6'
    assert INTERPRET("(defun MUL2 (x y z) (* (* x y) z)) (MUL2 2 2 2)") == '8'
    assert INTERPRET("(defun SUB2 (x y z) (- (- x y) z)) (SUB2 2 2 2)") == '-2'
except Exception as e:
    print(f"Test Block 17:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 17:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(define DS '((Don Smith) 45 3000 (August 25 1980)))") == '((DON SMITH) 45 3000 (AUGUST 25 1980))'
    assert INTERPRET("(car (cdr (cdr (cdr DS))))") == '(AUGUST 25 1980)'
    assert INTERPRET("(define a '((1 2 3 (4 (5 (6 (7))) 8) 9 (10 11) 12 13 (14 15) 16 17 18)))") == '((1 2 3 (4 (5 (6 (7))) 8) 9 (10 11) 12 13 (14 15) 16 17 18))'
    assert INTERPRET("(car(car(cdr(car(cdr(car(cdr(car(cdr(cdr(cdr(car a))))))))))))") == '7'
    assert INTERPRET("(cdr(car(cdr(cdr(cdr(cdr(cdr(car a))))))))") == '(11)'
except Exception as e:
    print(f"Test Block 18:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 18:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(cons 'to '(be or not))") == '(TO BE OR NOT)'
    assert INTERPRET("(cons '(to be) '(or not))") == '((TO BE) OR NOT)'
except Exception as e:
    print(f"Test Block 19:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 19:\t\033[92mPASSED\033[0m")
RESET()

try:
    assert INTERPRET("(defun two_to_the_power (n) (if (= n 0) 1 (* 2 (two_to_the_power (- n 1))))) (two_to_the_power 12)") == '4096'
except Exception as e:
    print(f"Test Block 20:\t\033[91mFAILED\033[0m")
    ERRORS += 1
else:
    print(f"Test Block 20:\t\033[92mPASSED\033[0m")
RESET()

print(f"\n{ERRORS} errors found")
print(f"Score: \033[4m\033[96m{int(((TESTS-ERRORS)/TESTS) * 100)}%\033[0m")