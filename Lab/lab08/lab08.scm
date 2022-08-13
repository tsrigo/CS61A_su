(define (over-or-under num1 num2) 
    '(if (= num1 num2) 0 (if (< num1 num2) -1 (if (> num1 num2) 1) ))
    (cond
        ((= num1 num2) 0)
        ((< num1 num2) -1)
        (else 1)
    )
)

(define (composed f g)
    (define (help x)
        (f (g x))
    )
    (lambda (x) (help x))
)

(define (square n) (* n n))

(define (pow base exp) 
    (cond
        ((= 1 base) 1)
        ((= 0 exp) 1)
        ((= 1 exp) base)
        (else 
            (if (even? exp)
                (pow (square base) (/ exp 2))
                (* base (pow base (- exp 1)))
            )
        )
    )
)

(define (ascending? lst) 
    (if (or (null? lst) (null? (cdr lst)))
        #t
        (and
            (or
                (< (car lst) (car (cdr lst)))
                (= (car lst) (car (cdr lst)))
            )
            (ascending? (cdr lst))
        )
    )
)
