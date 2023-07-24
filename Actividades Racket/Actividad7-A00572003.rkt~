#lang racket

;;Enlist: lst => lst
(define enlist
  (lambda (lst)
    (cond
    [(null? lst) '()]
    [(pair? lst) (cons (list (car lst)) (enlist (cdr lst)))]
    [else (list lst)]
    )))

(enlist '())
(enlist '(a b c))
(enlist '((1 2 3) 4 (5) 7 8))

;;Invert-pairs: lst => lst.
(define invert-pairs
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [else (cons
             (list (car( cdr (car lst))) (car (car lst)))
            (invert-pairs (cdr lst)))]
      )))

(invert-pairs '()) 
(invert-pairs '((a 1)(a 2)(b 1)(b 2)))
(invert-pairs '((January 1)(February 2)(March 3)))

;;deep-reverse: lst => lst.
(define deep-reverse
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [(list? (car lst)) (append (deep-reverse(cdr lst)) (cons (deep-reverse(car lst)) '()))]
      [else (append (deep-reverse (cdr lst)) (list (car lst)))]
      ))) 

(deep-reverse '())
(deep-reverse '(a (b c d) 3))
(deep-reverse '((1 2) 3 (4 (5 6))))
(deep-reverse '(a (b (c (d (e (f (g (h i j)))))))))


(define same
  (lambda (lst)
    (cond
      []

;;pack: lst=> lst.
(define pack
  (lambda (lst)
    (cond
      [(null?) '()]
      [= car cadr (append(cons(pack(car lst))))]