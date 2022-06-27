from operator import floordiv, mod

def divide_exact(n, d):
    ''' Return the quotient and remainder of dividing N by D. 
    
    >>> q，r = divide_ exact(2013, 10)
    >>> q
    201
    >>> r
    2
    '''
    return floordiv(n, d), mod(n, d)
