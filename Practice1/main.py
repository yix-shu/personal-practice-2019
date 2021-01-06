def tribonacci(signature, n):
  if (n==0):
    return []
    for x in range(n):
        if (n<=2):
            return signature[0:n]
        elif(x <= 2):
            pass
        else:
            signature.append(signature[x-3] + signature[x-2] + signature[x-1])
    return signature
print(tribonacci([300, 200, 100], 0))