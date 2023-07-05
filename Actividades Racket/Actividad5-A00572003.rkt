#lang racket

(define l1 '(1 2 3 4 -5 -6 4 3 4))

(define positive
  (lambda (lst)
    (cond
      [(empty? lst) 0]
      [(>= (car lst) 0) (+ 1 (positive (cdr lst)))]
      [else (positive (cdr lst))]
      )))

(positive l1)

(define find
  (lambda (lst b)
    (cond
      [(empty? lst) 0]
      [(= (car lst) b) (+ 1 (find (cdr lst) b))]
      [else (find (cdr lst) b)]
      )))

(find l1 4)
