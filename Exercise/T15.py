# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def prime_factorization():
    """
    Finds the prime factorization of a number n and prints it in the format
    p1^a1 * p2^a2 * ...
    """
    try:
        n = int(input())
    except (IOError, ValueError):
        return

    factors = []
    d = 2
    temp_n = n

    while d * d <= temp_n:
        if temp_n % d == 0:
            count = 0
            while temp_n % d == 0:
                count += 1
                temp_n //= d
            
            if count == 1:
                factors.append(str(d))
            else:
                factors.append(f"{d}^{count}")
        d += 1
    
    # اگر بعد از حلقه چیزی از عدد باقی مانده باشد، آن باقیمانده خودش یک عامل اول است
    if temp_n > 1:
        factors.append(str(temp_n))

    print("*".join(factors))

# برای اجرا، این تابع را فراخوانی کنید
prime_factorization()