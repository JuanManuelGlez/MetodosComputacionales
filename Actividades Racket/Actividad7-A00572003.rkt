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

(invert-pairs '((a 1)(a 2)(b 1)(b 2)))