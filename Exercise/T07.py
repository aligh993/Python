# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def ta_revenge_tiling():
    """
    Solves a tiling problem variation for a 3xN grid.
    The problem asks for the number of ways to tile a 3xN grid with 1x2 dominoes.
    The sample outputs (n=4 -> 22, n=10 -> 1142) suggest the answer is
    2 * a(n), where a(n) is the standard count for 3xN tiling.
    The standard recurrence is a(n) = 4*a(n-2) - a(n-4).
    """
    try:
        n = int(input())
    except (IOError, ValueError):
        return

    # اگر n فرد باشد، مساحت کل فرد است و نمی‌توان با دومینوهای 1x2 پوشاند
    if n % 2 != 0:
        print(0)
        return

    # استفاده از برنامه‌نویسی پویا برای محاسبه تعداد حالات
    # dp[i] تعداد حالات برای شبکه 3xi را ذخیره می‌کند
    dp = {0: 1, 2: 3} # مقادیر پایه
    
    # محاسبه مقادیر برای n های زوج بعدی
    for i in range(4, n + 1, 2):
        dp[i] = 4 * dp[i - 2] - dp[i - 4]
        
    # بر اساس خروجی نمونه، پاسخ نهایی دو برابر مقدار استاندارد است
    print(2 * dp[n])


# برای اجرا، این تابع را فراخوانی کنید
ta_revenge_tiling()