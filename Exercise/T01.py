# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def birth_date_separator():
    """
    Reads a 4-digit string for birth year and month,
    separates them, and prints them.
    """
    # ورودی نمونه: 7106
    input_string = input()
    
    # دو کاراکتر اول برای سال
    year = input_string[:2]
    
    # دو کاراکتر دوم برای ماه
    month = input_string[2:]
    
    # چاپ خروجی در فرمت خواسته شده
    print(f"saal: {year}")
    print(f"maah: {month}")

# برای اجرا، این تابع را فراخوانی کنید
birth_date_separator()