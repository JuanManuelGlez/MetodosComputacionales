#lang racket

#|
(define sumatoria
  (lambda (datos)
    (cond
      [(null? datos) 0]
      [else (+ (car datos) (sumatoria (cdr datos)))]
      )))|#


(define sum
  (lambda (n)
    (sum-aux n 0)))

(define sum-aux
  (lambda (n acum)
    (cond
      [(null? n) acum]
      [else (sum-aux (cdr n) (+ (car n) acum))]
      )))
#|
(define (incrementa datos)
  (if (null? datos)
      '()
      (cons (+ 1 (car datos) ) (incrementa (cdr datos)))
      ))|#

(define increment
  (lambda (datos)
    (increment-aux datos '() )))

(define increment-aux
  (lambda (datos acum)
    (cond
      [(null? datos) (reverse acum)]
      [else (increment-aux (cdr datos)(cons (+ 1 (car datos)) acum))]
      )))

(increment '(1 2 3 4))
    