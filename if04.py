def main(a,b,c):
    """
    Find number of positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    xotira = 0
    if a>0:
        xotira = xotira + 1
    if b>0:
        xotira = xotira + 1
    if c>0: 
        xotira = xotira + 1
    
    return xotira
print(main(12,-5,9))