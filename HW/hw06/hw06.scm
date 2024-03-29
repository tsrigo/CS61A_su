(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
    (car (cdr s))
)

(define (caddr s) 
    (car (cddr s))
)

(define (interleave lst1 lst2) 
    (define (help lst1 lst2 ans choose)
        (cond 
            ((null? lst1) 
                (define ans (append ans lst2))
                ans            
            )
            ((null? lst2) 
                (define ans (append ans lst1))
                ans            
            )

            ((= 1 choose)
                (define ans (append ans (list (car lst1))))
                (help (cdr lst1 ) lst2 ans 2)
            )
            ((= 2 choose)
                (define ans (append ans (list (car lst2))))
                (help lst1 (cdr lst2) ans 1)
            )
        )
    )
    (help lst1 lst2 nil 1)
)

(define (my-filter pred lst) 
    (define (help pred lst ans)
        (cond 
            ((null? lst) ans)
            (else 
                (if (pred (car lst)) (define ans (append ans (list (car lst)))))
                (help pred (cdr lst) ans)
            )
        )
    )
    (help pred lst nil)
)

(define (concatenate s) 
    (define (help s ans)
        (cond 
            ((null? s) ans)
            (else
                (define ans (append ans (car s)))
                (help (cdr s) ans)
            )
        )
    )
    (help s nil)
)
