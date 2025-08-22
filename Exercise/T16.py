# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

# توابع کمکی برای مسئله "جستجو در پدر"
def get_sum_of_digits(n):
    """Calculates the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))

def get_sum_of_distinct_prime_factors(n):
    """Calculates the sum of distinct prime factors of a number."""
    sum_factors = 0
    d = 2
    temp_n = n
    while d * d <= temp_n:
        if temp_n % d == 0:
            sum_factors += d
            while temp_n % d == 0:
                temp_n //= d
        d += 1
    if temp_n > 1:
        sum_factors += temp_n
    return sum_factors

def is_father_number():
    """
    For each input n, checks if there exists an x < n such that n is the "father" of x.
    Father(x) = D(x) = x + sum_digits(x) + sum_distinct_prime_factors(x).
    """
    try:
        t = int(input())
        for _ in range(t):
            n = int(input())
            found = False
            # باید چک کنیم آیا n پدرِ عددی کوچکتر از خودش هست
            for x in range(1, n):
                father_of_x = x + get_sum_of_digits(x) + get_sum_of_distinct_prime_factors(x)
                if father_of_x == n:
                    found = True
                    break
            if found:
                print("Yes")
            else:
                print("No")
    except (IOError, ValueError):
        return

# برای اجرا، این تابع را فراخوانی کنید
is_father_number()