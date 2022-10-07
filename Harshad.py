'''Harshad'''
def check(number):
    '''Harshad'''
    sumn = 0
    for iii in str(number):
        if iii == "-":
            iii = 0
        sumn += int(iii)
    if number == 0:
        print("No")
    elif number % sumn == 0:
        print("Yes")
    else:
        print("No")
    sumn = 0
def main():
    '''sdffds'''
    for _ in range(10):
        number = int(input())
        check(number)
main()
