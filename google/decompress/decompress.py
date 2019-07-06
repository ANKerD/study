l = 0
r = 0

def decomp(s):
    global l, r
    # print l,r
    while l < r and s[l] == ']':
        l += 1
    if l+1 >= r:
        return ''
    mul = 0
    while l < r and s[l].isdigit():
        mul = mul * 10 + int(s[l])
        l += 1
    word = ''
    while l < r and s[l].isalpha():
        word += s[l]
        l += 1
    if l < r and s[l] == '[':
        l+=1
    if word:
        ret = mul * word + decomp(s)
    else:
        ret = mul * decomp(s)
    return ret + decomp(s)

def eval(txt):
    global l,r
    l = 0; r = len(txt)
    t = decomp(txt)
    print txt, t
    return ''

try:
    
    print eval('3a')
    print eval('3[1a]')
    print eval('2b[3a]')
    print eval('1b[3a]2c')
    print eval('1b[3a[4p]]3c')
    print eval('3abv')
    print eval('3a6v')
    print eval('1b[3a[4p]]3c2m')
    print eval('1b[3a[4p]]3c2mo')
    print eval('4a4b4c')
except:
    pass
    print l,r