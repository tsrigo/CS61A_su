(define (tail-replicate x n)
    (define (help x n ans)
        (if (equal? n 0)
            ans
            (help x (- n 1) (cons x ans))
        )
    )
    (help x n nil)
)