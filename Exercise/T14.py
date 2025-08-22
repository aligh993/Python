# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import math

def is_perfect_number():
    """
    Checks if a number N is a perfect number.
    A number is perfect if it is equal to the sum of its proper divisors.
    """
    try:
        n = int(input())
    except (IOError, ValueError):
        return

    if n <= 1:
        print("NO")
        return

    # مجموع مقسوم‌علیه‌ها را با ۱ شروع می‌کنیم (چون ۱ همیشه مقسوم‌علیه است)
    sum_of_divisors = 1
    
    # برای پیدا کردن مقسوم‌علیه‌ها تا جذر عدد می‌رویم
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_of_divisors += i
            # اگر i مقسوم‌علیه باشد، n/i هم هست
            if i * i != n:
                sum_of_divisors += n // i
                
    if sum_of_divisors == n:
        print("YES")
    else:
        print("NO")

# برای اجرا، این تابع را فراخوانی کنید
is_perfect_number()