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
       (car (cdr (cdr (car list)))) ; Si la posicion del primer elemento del primer elemento es igual a la pos actual y el segundo elemento es igual a la letra, regresa el tercer elemento 
          )]
      [else (compara (cdr list) letra pos)]
      )))

(define valida
  (lambda (list entrada pos fin)
    (cond
      [(null? entrada) (final pos fin)]
      [(= -1 pos) #f]
      [else (valida list (cdr entrada) (compara list (car entrada) pos) fin)]
      )))

(define final
  (lambda (pos fin)
    (cond
      [(null? fin) #F]
      [(= pos (car fin)) #T]
      [else (final pos (cdr fin))]
      )))

(define recorreLista
  (lambda (list entradas pos fin result)
    (cond
      [(null? entradas) (deep-reverse result)]
      [else 
            (recorreLista list (cdr entradas) pos fin (cons (valida list (car entradas) pos fin) result))]
      )))

(define deep-reverse
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [(list? (car lst)) (append (deep-reverse(cdr lst)) (cons (deep-reverse(car lst)) '()))]
      [else (append (deep-reverse (cdr lst)) (list (car lst)))]
      )))

(define inputs
  (lambda (automata entradas)
    (cond
      [(null? automata) -1]
      [(null? entradas) -1]
      [else (recorreLista (caddr automata) entradas (car (cdr (cdr(cdr automata)))) (car (cdr (cdr(cdr(cdr automata))))) '() ) ]
      )))


(define automata
  '( (0 1 2 3 4)                         ; Conjunto de estados
     (a b)                               ; Alfabeto de entrada
     ((0 a 1) (0 b 2) (1 a 1) (1 b 3)    ; Transiciones
      (2 b 2) (2 a 1) (3 a 1) (3 b 4)
      (4 a 1) (4 b 2))
     0                                   ; Pos
     (4)                                 ; Fin
   ))

(define entradas
  '( (a b a b a a b b a b b) (a a a a a a b) (a b a b a b b) (a b) (a b b) )
)

(inputs automata entradas)



      

