def createAlarm(h, m, s, desc):
    return (int(h), int(m), int(s), desc)

def equal(h1, m1, s1, h2, m2, s2):
    if (int(h1) == int(h2) and int(m1) == int(m2) and int(s1) == int(s2)):
        return True
    return False

def addTime(h1, m1, s1, h2, m2, s2):
    s3 = int(s1) + int(s2)
    m3 = s3/60 + int(m1) + int(m2)
    h3 = int(h1) + int (h2) + m3/60

    s3 %= 60
    m3 %= 60
    return (int(h3), int(m3), int(s3))
