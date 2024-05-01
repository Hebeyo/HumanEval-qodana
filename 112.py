def reverse_delete(s,c):
    for i in c:
        s=s.replace(i,'')
    return (s,s[::-1] == s)
