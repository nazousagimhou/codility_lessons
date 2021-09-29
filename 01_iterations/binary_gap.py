decimal_number = 578


def solution(N):
    binary = format(N, 'b')
    print(binary)
    binary_gap = 0
    max_bg = 0
    for bit in binary:
        if bit == "0":
            binary_gap = binary_gap + 1
        else:
            if binary_gap > max_bg:
                max_bg = binary_gap
            print(f'binary gap actual {binary_gap}')
            binary_gap = 0
            print(f'reseteando el binary gap')
    print(f'este es el maximo binary gap {max_bg}')
    print(binary_gap)
    return max_bg


if __name__ == '__main__':
    result = solution(decimal_number)
    print(result)