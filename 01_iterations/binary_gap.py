decimal_number = 16

def solution(N):
    binary = format(N,'b')
    binary_gap = 0
    for bit in binary:
        max_binary_gap = binary_gap + 1
        print(max_binary_gap)



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