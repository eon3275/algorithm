def solution(phone_book):
    hash = {}
    for n in phone_book:
        hash[n] = True
    for n in phone_book:
        prefix = ''
        for digit in n:
            prefix+=digit
            if prefix in hash and prefix!=n:
                return False
    return True