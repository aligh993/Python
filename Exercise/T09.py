# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import math

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    # برای چک کردن اول بودن n، کافیست تقسیم‌پذیری آن را تا جذر n بررسی کنیم
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range():
    """
    Finds and prints all prime numbers within a given range [a, b].
    """
    try:
        a = int(input())
        b = int(input())
        # a, b = map(int, input().split())
    except (IOError, ValueError):
        return
        
    prime_numbers = []
    # حلقه از a تا b برای پیدا کردن اعداد اول
    for num in range(a + 1, b + 1):
        if is_prime(num):
            prime_numbers.append(str(num))
            
    # چاپ اعداد پیدا شده با کاما بین آن‌ها
    print(",".join(prime_numbers))

# برای اجرا، این تابع را فراخوانی کنید
find_primes_in_range()