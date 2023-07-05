#lang racket


;;Juan Manuel González Ascencio. A00572003.
(define digitos
  (lambda (amount)
    (cond
    [(= 0 (quotient amount 10)) 1]
    [else (+ 1 (digitos (quotient amount 10)))]
    )))

(digitos 1243)

;;Factorial: num=> num

(define factorial
  (lambda (number)
    (cond
      [(= 0 number) 1]
      [else (* number ( factorial (- number 1)))]
      )))

(factorial 0)
(factorial 5)
(factorial 40)

;;Pow: num, num => num

(define pow
  (lambda (number exp)
    (cond
      [(= 0 exp) 1]
      [else (* number (pow number (- exp 1)))]
      )))

(pow 5 0)
(pow -5 3)
(pow 15 12)

;;fib: num => num

(define fib
  (lambda (n)
    (cond
      [(<= n 2) 1]
      [else (+ (fib (- n 1)) (fib (- n 2)))]
      )))

(fib 6)
(fib 42)