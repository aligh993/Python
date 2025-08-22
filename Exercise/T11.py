# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def is_palindrome_number():
    """
    Checks if a given number is a palindrome.
    """
    try:
        n_str = input()
        # ساده‌ترین راه: رشته را با معکوس خودش مقایسه کن
        if n_str == n_str[::-1]:
            print("YES")
        else:
            print("NO")
    except IOError:
        return

# برای اجرا، این تابع را فراخوانی کنید
is_palindrome_number()