def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    x=a
    if a<x:
        x=a
    if b<x:
        x=b
    if c<x:
        x=c
    return x
print(main(2,4,1))