#lang racket

;;fahrenheit-to-celsius: Num =>Num
(define fahrenheit-to-celsius
  (lambda (f)
    (/(*(- f 32)5)9)))

(fahrenheit-to-celsius 212)
(fahrenheit-to-celsius 32)
(fahrenheit-to-celsius -40)

;;roots: num,num,num=>num
(define roots
  (lambda (a b c)
    (/(+(* -1 b)(sqrt(-(* b b)(* 4 a c))))(* 2 a))))

(roots 2 4 2)
(roots 1 0 0)
(roots 4 5 1)