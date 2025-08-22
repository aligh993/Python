# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import math

# تابع فاکتوریل
def fact(n):
    if n < 0: return 0
    return math.factorial(n)

# تابع ترکیب (n choose k)
def comb(n, k):
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)
    # پیاده‌سازی دستی: return fact(n) // (fact(k) * fact(n - k))

# تابع محاسبه سری خواسته شده
def calc_series(n):
    """
    Calculates the series: Sum_{i=1 to n} [ Product_{j=1 to i} [ Comb(i, j) ] ]
    The formula in the PDF seems to have i and j swapped.
    Based on the sample case (n=3 -> 12), the formula above is correct.
    """
    total_sum = 0
    for i in range(1, n + 1):
        inner_product = 1
        for j in range(1, i + 1):
            inner_product *= comb(i, j)
        total_sum += inner_product
    return total_sum

def main_series_calculation():
    try:
        n = int(input())
        result = calc_series(n)
        print(result)
    except (IOError, ValueError):
        return

# برای اجرا، این تابع را فراخوانی کنید
main_series_calculation()