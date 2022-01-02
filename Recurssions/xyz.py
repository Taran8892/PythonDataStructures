
def stringConcat(a='taranjeet', b='singh'):
    if len(a) > len(b):
        return(b+a+b)
    else:
        return(a+b+a)

print(stringConcat())