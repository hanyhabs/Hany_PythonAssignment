def mutate_string(string, position, character):
    li = list(string)
    li[position]=character
    s=''.join(li)
    return s

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)