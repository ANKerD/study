def decomp(s, l=0, r=None):
    if not r: r = len(s)-1
    if l >= r:
        return ''
    mul = 0
    while s[l].isdigit():
        mul = mul * 10 + int(s[l])
        l += 1
    word = ''
    while l <= r and s[l].isalpha():
        word += s[l]
        l += 1
    if word:
        ret = mul * word + decomp(s, l+1, r)
    else:
        ret = mul * decomp(s, l+1, r)
    return ret

def eval(txt):
    t = decomp(txt)
    return t

print eval('3a')
print eval('1b[3a]')
print eval('1b[3a]2c')
print eval('1b[3a[4p]]3c')