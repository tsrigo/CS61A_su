(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  (define (help s idx ans)
    (if (null? s)
      ans
      (begin 
        (define now (list (list idx (car s))))
        (define ans (append ans now))
        (help (cdr s) (+ idx 1) ans)
      )
    )
  )
  (help s 0 nil)
)

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? list1 list2)
  ; BEGIN PROBLEM 16
  'replace-this-line
  )
  ; END PROBLEM 16

