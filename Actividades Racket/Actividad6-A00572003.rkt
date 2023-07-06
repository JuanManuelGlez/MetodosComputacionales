#lang racket

;;Duplicate: lst => lst
(define duplicate
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [else (cons (car lst) (cons (car lst) (duplicate (cdr lst))))]
      )))


(duplicate '())
(duplicate '(1 2 3))
(duplicate '(a b c d e f g h))

;;Positives: lst =>lst
(define positives
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [(> (car lst) 0) (cons (car lst) (positives (cdr lst)))]
      [else (positives (cdr lst))]
      )))

(positives '())
(positives '(12 -4 3 -1 -10 -13 6 -5))
(positives '(-4 -1 -10 -13 -5)) 

;;symbols: lst => bool
(define symbols
  (lambda (lst)
    (cond
    [(null? lst) #t]
    [(number? (car lst)) #f]
    [else (symbols (cdr lst))]
    )))

(symbols '())
(symbols '(a e i o u ))
(symbols '(a b c d 42 e))

;;swappper: int int list => list
(define swapper
  (lambda (a b lst)
    (cond
      [(null? lst) '()]
      [(= (car lst) a) (cons b (swapper a b (cdr lst)))]
      [(= (car lst) b) (cons a (swapper a b (cdr lst)))]
      [else (cons (car lst) (swapper a b (cdr lst)))]
      )))

(swapper 1 2 '())
(swapper 1 2 '(4 4 5 2 4 8 2 5 6 4 5 1 9 5 9 9 1 2 2 4))
(swapper 1 2 '(4 3 4 9 9 3 3 3 9 9 7 9 3 7 8 7 8 4 5 6))

      
;; dot: lst, lst => num
(define dot
  (lambda (lst1 lst2)
    (cond
      [(null? lst1) 0]
      [else (+ (* (car lst1) (car lst2)) (dot (cdr lst1) (cdr lst2)))]
      )))

(dot '() '())
(dot '(1 2 3) '(4 5 6))
(dot '(1.3 3.4 5.7 9.5 10.4) '(-4.5 3.0 1.5 0.9 0.0)) 