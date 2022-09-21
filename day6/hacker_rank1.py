def swap_case(s):
    k=''
    for i in range(len(s)):
        if(s[i].isupper() ):
            k+=s[i].lower()
            
        else:
            k+=s[i].upper()
    return k

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)