def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    bools = [True if isinstance(x,list) else False for x in lst]
    if False in bools:
        return False
    else:
        return True