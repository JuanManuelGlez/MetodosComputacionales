#lang racket

(define sign
  (lambda (n)
    (cond
      [(< n 0) -1 ]
      [(= n 0) 0]
      [(> n 0) 1]
      )))

(sign -5)
(sign 10)
(sign 0)

(define bmi
  (lambda (weight height)
    (let
        ((result (/ weight (expt height 2))))
      (cond
        [(< result 20) 'underweight]
        [(< result 25) 'normal]
        [(< result 30) 'obese1]
        [(< result 40) 'obese2]
        [else 'obese3]))))

(bmi 45 1.5)
(bmi 55 1.5)
(bmi 76 1.7)
(bmi 81 1.6)
(bmi 120 1.6)