def real_line():
    real_line_by = []
    real_line_by12 = """
    ------A-------B------C------D------E----O--F----G---H---I---J----K----L---M---N----P---Q---
    ---(-5/12)-(-1/3)-(-1/4)-(-1/6)-(-1/12)-0-1/12-1/6-1/4-1/3-5/12-1/2--2/3-3/4-5/6-11/12-1--->

    Points (géométrie)| A   | B  | C   | D   | E   | O | F  | G  | H  | I | J  | K | L  | M  | N  |
    ------------------|-----|----|-----|-----|-----|---|----|----|----|---|----|---|----|----|----|
    Abscisses (nombre)|-5/12|-1/3|-1/4 |-1/6 |-1/12| 0 |1/12| 1/6| 1/4|1/3|5/12|1/2|2/3 |3/4 |5/6 |
    ------------------|-----|----|-----|-----|-----|---|----|----|----|---|----|---|----|----|----|
    Approximations    |-0.42|-0.3|-0.25|-0.17|-0.08| 0 |0.08|0.17|0.25|0.3|0.42|0.5|0.67|0.75|0.83|
    """
    real_line_by.append(real_line_by12)
    real_line_by10 = """
    ------A------B------C------D------E---O--F---G---H---I---J---K---L---M---N--P----
    ---(-0.5)-(-0.4)-(-0.3)-(-0.2)-(-0.1)-0-0.1-0.2-0.3-0.4-0.5-0.6-0.7-0.8-0.9-1--->
    """
    real_line_by.append(real_line_by10)
    real_line_by5 = """
    ------A------B-----C-----D------E------F------G---O--H---I---J---K--L--M---N---P-----
    ---(-1.4)-(-1.2)-(-1)-(-4/5)-(-3/5)-(-2/5)-(-1/5)-0-1/5-2/5-3/5-4/5-1-1.2-1.4-1.6--->
    """
    real_line_by.append(real_line_by5)
    real_line_by3 = """
    -----A-----B------C-----D-----E------F---O--G---H--I--J---K--L----
    ---(-2)-(-5/3)-(-4/3)-(-1)-(-2/3)-(-1/3)-0-1/3-2/3-1-4/3-5/3-2--->
    """
    real_line_by.append(real_line_by3)
    real_line_by2 = """
    -----A-----B-----C-----D-----E-----F---O--G--H--I--J--K--L----
    ---(-3)-(-2.5)-(-2)-(-1.5)-(-1)-(-1/2)-0-1/2-1-1.5-2-2.5-3--->
    """
    real_line_by.append(real_line_by2)
    return real_line_by

def equilateral():
    equilat_pics = []
    dessin = """
                  A
                 / \\   
                /   \\
               /     \\ 
              /       \\   
             /         \\
            B-----------C
    """
    equilat_pics.append(dessin)
    dessin = """
         A
        / \\   
       /   \\
    1 /     \\ 1
     /       \\   
    /         \\
    B----------C
         1
    """
    equilat_pics.append(dessin)
    dessin = """
          A
         / \\   < CAB = (AB ^ AC) = π/3
        /   \\
       /     \\ 
      /       \\     < BCA = (CA ^ CB) = π/3
     /)       (\\     
    B-----------C
            
    < ABC = (BC ^ BA) = π/3
    """
    equilat_pics.append(dessin)
    dessin = """
          A
         /|\\
        / | \\
    1  /  |  \\ 1
      /   |   \\   
     /    |    \\
    B-----H------C
     0.5     0.5    
    """
    equilat_pics.append(dessin)
    dessin = """
          A
         /|
        / |
    1  /  | √3/2 ~ 0.87
      /   |
     /    |
    B-----H
    1/2 = 0.5  
    """
    equilat_pics.append(dessin)
    dessin = """
          A  < BAH = (AB ^ AH) = π/6
         /|
        / |
    1  /  | √3/2 ~ 0.87
      /   |
     /    |  < ABH = (BH ^ BA) = π/3
    B-----H
    1/2 = 0.5  
    """
    equilat_pics.append(dessin)
    dessin = """
          A  < BAH = (AB ^ AH) = π/6
         /|
        / |                 cos(π/6) = √3/2 = sin(π/3)
    1  /  | √3/2 ~ 0.87     sin(π/6) = 1/2 = cos(π/3)
      /   |
     /    |  < ABH = (BH ^ BA) = π/3
    B-----H
    1/2 = 0.5  
    """
    equilat_pics.append(dessin)
    return equilat_pics

def square():
    square_pics = []
    dessin = """
    D-----------C
    |           |
    |           |
    |           |
    |           |
    |           |
    A-----------B
    """
    square_pics.append(dessin)
    dessin = """
          1
    D-----------C
    |           |
    |           |
  1 |           | 1
    |           |
    |           |
    A-----------B
          1
    """
    square_pics.append(dessin)
    dessin = """
          
    D-----------C 
    |π/2     π/2|
    |           | 
    |           | 
    |           |
    |π/2     π/2|
    A-----------B
          
    """
    square_pics.append(dessin)
    dessin = """
          
             C
            / |  < BCA = (CA ^ CB) = π/4
           /  |
          /   |
         /    |
        /     |
       A------B
          
    """
    square_pics.append(dessin)
    dessin = """
          
             C
            / |  < BCA = (CA ^ CB) = π/4
           /  |
    √2    /   |  1 
         /    |      \u26A0 AB = BC bien que le dessin soit faux
        /     |
       A------B
          1
    """
    square_pics.append(dessin)
    dessin = """
          
             C
            / |  < BCA = (CA ^ CB) = π/4
           /  |   
    √2    /   |  1 \u26A0 AB = BC = 1 bien que le dessin soit faux
         /    |      
        /     |    \u27A1 cos(π/4) = cos(BCA) = BC / AC = 1/√2 = √2/2 ~ 0.707
       A------B
          1
    """
    square_pics.append(dessin)
    dessin = """
          
             C
            / |  < BCA = (CA ^ CB) = π/4
           /  |   
    √2    /   |  1 \u26A0 AB = BC = 1 bien que le dessin soit faux
         /    |      
        /     |    \u27A1 cos(π/4) = cos(BCA) = BC / AC = 1/√2 = √2/2 ~ 0.707
       A------B
          1        \u27A1 sin(π/4) = cos(BCA) = AB / AC = 1/√2 = √2/2 ~ 0.707
    """
    square_pics.append(dessin)
    return square_pics
    
def circles():
    circle0 = """
                  0
                00 00 
             00 00 00 00 
          00 00 00 00 00 00 
       00 00 00 00 00 00 00 00 
       00 00 00 00 00 00 00 00
     0 00 00 00 00 00 00 00 00 0
       00 00 00 00 00 00 00 00
       00 00 00 00 00 00 00 00
          00 00 00 00 00 00 
             00 00 00 00 
                00 00
                  0
    """
    return circle0

def intervalles():
    zero_un = []
    zero_un_12 = """
           A     O     B       I   C
    -------|-----[-----|-------]---|--------->
    -1  -5/12    0    5/12     1  15/12      2
    
    -5/12\u220A]-\u221E; 0[    5/12\u220A[0; 1]   15/12\u220A]1; +\u221E[
    """
    zero_un.append(zero_un_12)
    zero_un_10 = """
           A     O     B     I     C
    -------|-----[-----|-----]-----|----->
    -1   -0.5    0    0.5    1    1.5    2
    
    -0.5\u220A]-\u221E; 0[    0.5\u220A[0; 1]   1.5\u220A]1; +\u221E[
    """
    zero_un.append(zero_un_10)
    zero_un_5 = """
           A     O     B     I     C
    -------|-----[-----|-----]-----|----->
    -1   -0.2    0    1/5    1    1.2    2
    
    -1/5\u220A]-\u221E; 0[    0.2\u220A[0; 1]   6/5\u220A]1; +\u221E[
    """
    zero_un.append(zero_un_5)
    zero_un_3 = """
           A   O B  I  C
    -------|---[-|--]--|---->
          -1   0 1/3  5/3   3
    
    -1\u220A]-\u221E; 0[    1/3\u220A[0; 1]   5/3\u220A]1; +\u221E[
    """
    zero_un.append(zero_un_3)
    zero_un_2 = """
           A   O B I  C
    -------|---[-|-]--|---->
         -3/2  0 1/2  2    4
    
    -1.5\u220A]-\u221E; 0[    1/2\u220A[0; 1]   2\u220A]1; +\u221E[
    """
    zero_un.append(zero_un_2)
    return zero_un

    