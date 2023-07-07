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