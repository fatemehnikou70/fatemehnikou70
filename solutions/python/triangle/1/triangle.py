def is_valid (a, b, c):
    if a<=0 or b<=0 or c<=0:             #شرط مثبت بودن ضلع ها#
        return False
    if a + b <= c or a + c <= b or b + c <= a :        #شرط مثلث بودن#
        return False
    else:
        return True
    
    
def equilateral(sides):
    a, b, c = sides
    if not is_valid(a,b,c):
        return False
    
    elif a == b == c:
        return True
    else:
        return False
    
def isosceles(sides):
    a, b, c = sides
    if not is_valid(a,b,c):
        return False
    elif a == b or b == c or a == c:
        return True
    else:
        return False


def scalene(sides):
    a, b, c = sides
    if not is_valid(a,b,c):
        return False
    elif a != b and a!= c and b!=c:
        return True
    else:
        return False
    
