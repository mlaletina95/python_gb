import doctest


def delete_non_alphabet_and_spaces(s: str):
    """
    >>> delete_non_alphabet_and_spaces('hello world b a')
    'hello world b a'

    >>> delete_non_alphabet_and_spaces('HELLO WORLD B A')
    'hello world b a'

    >>> delete_non_alphabet_and_spaces('hello, world: b, a!')
    'hello world b a'

    >>> delete_non_alphabet_and_spaces('hello world b aцш!')
    'hello world b a'

    >>> delete_non_alphabet_and_spaces('HELLO, world: b, a,цш!')
    'hello world b a'
    """
    res = ""

    l = len(s)
    for i in range(l):
        c = s[i].lower()
        if 'a' <= c <= 'z' or c == ' ':
            res += c

    return res


doctest.testmod(verbose=True)