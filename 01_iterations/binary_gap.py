decimal_number = 16

def solution(N):
    binary = format(N,'b')
    binary_gap = 0
    for bit in binary:
        if bit == "0":
            print(f'cero')
        else:
            print(f'uno')


if __name__=='__main__':
    result = solution(decimal_number) 
    print(result)



#print(type(result))
 #if bit == 0:
 #           print(max_binary_gap = max_binary_gap+1)
 #       else:
 #           print(f'{decimal_number} does not have a binary gap')
 #   return print(binary)
    #return bin(N)