'''RightArrow'''
def main():
    '''RightArrow'''
    kkk = int(input())
    nnn = int(input())
    num = 0
    sumn = 0
    for _ in range(nnn):
        num += 1
        print(" "*sumn + (kkk * "*"))
        if num > nnn/2:
            sumn -= 1
        else:
            sumn += 1
main()
