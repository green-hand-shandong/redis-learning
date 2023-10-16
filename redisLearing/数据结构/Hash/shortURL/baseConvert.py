def base10_to_base36(num): # 进制转换
    alphabets = "0123456789ABCDEFGHIJKOPQRSTUVWXYZ"
    result = ""
    while num != 0:
        num, i =divmod(num, 36)
        result = (alphabets[i]+result)
    
    return result or alphabets[0]