# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def print_digits_repeatedly():
    """
    Reads a number as a string and for each digit, prints that digit
    repeated by its own value.
    """
    try:
        num_str = input()
    except IOError:
        return
        
    for char_digit in num_str:
        digit_val = int(char_digit)
        # با استفاده از ضرب رشته، کاراکتر به تعداد مقدار عددی‌اش تکرار می‌شود
        repeated_digits = char_digit * digit_val
        print(f"{char_digit}: {repeated_digits}")

# برای اجرا، این تابع را فراخوانی کنید
print_digits_repeatedly()