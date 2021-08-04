decimal_number = 16

def solution(N):
    binary = format(N,'b')
    binary_gap = 0
    for bit in binary:
        if bit == "0":
            print(f'cero')
            binary_gap = binary_gap + 1
        else:
            print(f'uno')
    print(binary_gap)


if __name__=='__main__':
    result = solution(decimal_number) 
    print(result)

