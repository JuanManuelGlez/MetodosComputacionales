#lang racket

(define args-swap
  (lambda (f)
    (lambda (x y)
      (f y x)
      )))

((args-swap list) 1 2)
((args-swap /) 8 2)
((args-swap cons) '(1 2 3) '(4 5 6)) 
((args-swap map) '(-1 1 2 5 10) /)

(define there-exists-one?
  (lambda (f lst)
      (cond
        [(empty? lst) #f]
        [(f (car lst)) #t]
        [else (there-exists-one? f (cdr lst))]
        )))

(there-exists-one? positive? '())
(there-exists-one? positive? '(-1 -10 4 -5 -2 -1))
(there-exists-one? negative? '(-1))
(there-exists-one? symbol? '(4 8 15 16 23 42))
(there-exists-one? symbol? '(4 8 15 sixteen 23 42))

(define linear-search-aux
  (lambda (lst  x eq-fun acum)
    (cond
      [(empty? lst) #f]
      [(eq-fun x (car lst)) acum]
      [else (linear-search-aux (cdr lst) x eq-fun (+ 1 acum))]
      )))

(define linear-search
  (lambda (lst  x eq-fun)
    (linear-search-aux lst x eq-fun 0)))

(linear-search '() 5 =)
(linear-search '(48 77 30 31 5 20 91 92 69 97 28 32 17 18 96) 5 =)
(linear-search '("red" "blue" "green" "black" "white") "black" string=?)
(linear-search '(a b c d e f g h) 'h equal?)