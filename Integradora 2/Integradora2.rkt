#lang racket
#| Juan Manuel González Ascencio
Matricula: A00572003
Descripcion: programa que reciba como entrada la descripción de un autómata y una lista de entradas a validar, la función regresa una lista indicando si las diversas funciones se aceptan o no.
|#

(define compara
  (lambda (list letra pos)
    (cond
      [(null? list) -1]
      [(and (equal? pos (car (car list)))
            
         (equal? letra (car (cdr (car list))))
       (car (cdr (cdr (car list)))) 
          )]
      [else (compara (cdr list) letra pos)]
      )))

(define valida
  (lambda (list entrada pos fin)
    (cond
      [(empty? entrada) pos]
      [(= pos -1) #f]
      [else (compara list (car entrada) pos) (valida list (cdr entrada) pos fin)]
      )))

(valida '((0 a 1) (0 b 2) (1 a 1) (1 b 3) (2 b 2) (2 a 1) (3 a 1) (3 b 4) (4 a 1) (4 b 2)) '(a b a b a a b b) 0 4)




      

