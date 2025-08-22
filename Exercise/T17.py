# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def fibonacci_sum_representation():
    """
    Represents a number n as a sum of distinct Fibonacci numbers (Zeckendorf's theorem).
    Prints the indices of the Fibonacci numbers used.
    The problem uses a shifted Fibonacci sequence: 1, 2, 3, 5, 8, ...
    where F_1=1, F_2=2, etc.
    """
    try:
        n = int(input())
    except (IOError, ValueError):
        return

    if n == 0:
        print("0")
        return

    # ساخت دنباله فیبوناچی (با اندیس‌گذاری مسئله) تا جایی که از n بزرگتر نشود
    fib_nums = [1, 2]
    while fib_nums[-1] <= n:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    
    # آخرین عدد اضافه شده بزرگتر از n است، پس آن را حذف می‌کنیم
    if fib_nums[-1] > n:
        fib_nums.pop()

    result_indices = []
    # با روش حریصانه از بزرگترین عدد فیبوناچی شروع می‌کنیم
    for i in range(len(fib_nums) - 1, -1, -1):
        fib_val = fib_nums[i]
        if n >= fib_val:
            n -= fib_val
            # اندیس در مسئله از ۱ شروع می‌شود و با اندیس لیست (که از ۰ شروع می‌شود) ۱ واحد اختلاف دارد
            result_indices.append(str(i + 1))
    
    print(" ".join(result_indices))

# برای اجرا، این تابع را فراخوانی کنید
fibonacci_sum_representation()