"""Compound interest factors for lazy people like me"""


def fpin(i, n):
    """The convert present worth to future worth one

    Args:
        i: interest rate in decimal
        n: number of periods or whatever

    Returns:
        The convert present worth to future worth factor thing
    """
    return (1+i)**n


def pain(i, n):
    """The convert annuity to present worth one

    Args:
        i: interest rate in decimal
        n: number of periods or something

    Returns:
        pain
    """
    return (fpin(i,n)-1)/(fpin(i,n)*i)


def apin(i, n):
    """The opposite of pain

    Args:
        i: decimal interest rate
        n: # of periods

    Returns:
        inverse pain
    """
    return 1/pain(i,n)


def pfin(i, n):
    """Convert future worth to present worth

    Args:
        i: interest rate in decimal
        n: # of periods

    Returns:
        Conversion factor for changing future worth to present worth
    """
    return 1/fpin(i,n)


def fain(i, n):
    """Uniform series compound amount factor

    Also known as the convert an annuity to a future worth factor

    Args:
        i: same as everywhere else
        n: same as everywhere else
    Returns:
        a number
    """
    return (fpin(i,n) - 1) / i


def afin(i,n):
    """Sinking fun factor"""
    return 1/fain(i,n)


def cap_recov(p, s, i, n):
    """Capital recovery factor

    Args:
        p: The present worth of the thing
        s: The thing's salvage value after n years
        i: decimal interest rate
        n: # of compounding periods

    Returns:
        Whatever the capital recovery factor thing means
    """
    return (p-s)*apin(i,n) + s*i
