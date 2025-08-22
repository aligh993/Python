# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def sum_large_numbers():
    """
    Reads n large numbers and prints their sum. Python's arbitrary-precision
    integers handle this automatically.
    """
    try:
        num_count = int(input())
        total_sum = 0
        for _ in range(num_count):
            large_number = int(input())
            total_sum += large_number
        print(total_sum)
    except (IOError, ValueError):
        # در صورتی که ورودی خالی یا نامعتبر باشد
        return

# برای اجرا، این تابع را فراخوانی کنید
sum_large_numbers()