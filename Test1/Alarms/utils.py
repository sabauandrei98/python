def isTime(h, m, s):
    '''
    :param n: any type of data
    :return: True if positive number,
             False otherwise
    '''

    try:
        h1 = int(h)
        m1 = int(m)
        s1 =  int(s)
        if h1 >= 0 and h1 <= 24 and m1 >= 0 and m1 <= 59 and s1 >= 0 and s1 <= 59:
            return True
        else:
            return False
    except:
        return False
