#lang racket
#| Juan Manuel González Ascencio
Matricula: A00572003
Descripcion: programa que reciba como entrada la descripción de un autómata y una lista de entradas a validar, la función regresa una lista indicando si las diversas funciones se aceptan o no.
|#

;Función que sirve para comparar si las letras y las posiciones son correctas, regresa la siguiente posicion en caso de que si y #f si no.
;Solo funciona con una letra
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

;Esta función permite que compara pueda comparar una lista de letras
(define valida
  (lambda (list entrada pos fin)
    (cond
      [(null? entrada) (final pos fin)]
      [(= -1 pos) #f]
      [else (valida list (cdr entrada) (compara list (car entrada) pos) fin)]
      )))
; la funcion valida si la posición en donde estamos es un estado de aceptación
(define final
  (lambda (pos fin)
    (cond
      [(null? fin) #F]
      [(= pos (car fin)) #T]
      [else (final pos (cdr fin))]
      )))

;esto permite tener varias listas de entradas y se comunica con la función valida
(define recorreLista
  (lambda (list entradas pos fin result)
    (cond
      [(null? entradas) (deep-reverse result)]
      [else 
            (recorreLista list (cdr entradas) pos fin (cons (valida list (car entradas) pos fin) result))]
      )))
;Al usar un cons para meter elementos a la lista se ponen siempre al inicio, por lo que es necesario voltear la lista 
(define deep-reverse
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [(list? (car lst)) (append (deep-reverse(cdr lst)) (cons (deep-reverse(car lst)) '()))]
      [else (append (deep-reverse (cdr lst)) (list (car lst)))]
      )))
;Rompe los inputs para que la función recorrelista las entienda 
(define inputs
  (lambda (automata entradas)
    (cond
      [(null? automata) -1]
      [(null? entradas) -1]
      [else (recorreLista (caddr automata) entradas (car (cdr (cdr(cdr automata)))) (car (cdr (cdr(cdr(cdr automata))))) '() ) ]
      )))


(define automata
  '( (0 1 2 3 4) (a b) ((0 a 1) (0 b 2) (1 a 1) (1 b 3) (2 b 2) (2 a 1) (3 a 1) (3 b 4) (4 a 1) (4 b 2)) 0 (4)))

(define entradas
  '( (a b a b a a b b a b b) (a a a a a a b) (a b a b a b b) (a b) (a b b) (hola) )
)

(inputs automata entradas)



      

