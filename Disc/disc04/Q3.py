def best_k_segmenter(k, score):
    """
    >>> largest_digit_getter = best_k_segmenter(1, lambda x: x)
    >>> largest_digit_getter(12345)
    5
    >>> largest_digit_getter(245351)
    5
    >>> largest_pair_getter = best_k_segmenter(2, lambda x: x)
    >>> largest_pair_getter(12345)
    45
    >>> largest_pair_getter(245351)
    53
    >>> best_k_segmenter(1, lambda x: -x)(12345)
    1
    >>> best_k_segmenter(3, lambda x: (x // 10) % 10)(192837465)
    192
    """
    partitioner = lambda x: (x // pow(10, k), x % pow(10, k))
    def best_getter(n):
        assert n > 0
        best_seg = partitioner(n)[1]
        while n != 0:
            n, seg = partitioner(n)
            if score(seg) > score(best_seg):
                best_seg = seg
        return best_seg
    return best_getter

