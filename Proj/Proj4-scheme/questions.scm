(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  (define (help s idx)
    (if (null? s)
      nil
      (cons (list idx (car s)) (help (cdr s) (+ idx 1)))
    )
  )
  (help s 0)
)

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? list1 list2)
  (if (or (null? list1) (null? list2)) 
    (append list1 list2)
    (if (ordered? (car list1) (car list2))
      (cons (car list1) (merge ordered? (cdr list1) list2))
      (cons (car list2) (merge ordered? list1 (cdr list2)))
    )
  )
)

