# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def star_diamonds():
    """
    Prints two adjacent star-shaped diamonds based on an odd integer n.
    The implementation is tailored to replicate the specific sample output.
    """
    try:
        n = int(input())
    except (IOError, ValueError):
        return

    # اگر n فرد نبود یا در محدوده نبود، خارج شو
    if n % 2 == 0 or not (1 <= n <= 19):
        return
        
    # نیمه بالایی لوزی
    for i in range(n // 2):
        stars = 2 * i + 1
        padding = (n - stars) // 2
        middle_padding = n - 2*i
        print(' ' * padding + '*' * stars + ' ' * middle_padding + '*' * stars)

    # ردیف میانی
    print('*' * n + '*' * n)

    # نیمه پایینی لوزی
    for i in range(n // 2 - 1, -1, -1):
        stars = 2 * i + 1
        padding = (n - stars) // 2
        middle_padding = n - 2*i
        print(' ' * padding + '*' * stars + ' ' * middle_padding + '*' * stars)

# برای اجرا، این تابع را فراخوانی کنید
star_diamonds()