# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def find_pythagorean_triple_with_sum_n():
    """
    Finds a Pythagorean triple (a, b, c) such that a + b + c = n.
    """
    try:
        n = int(input())
    except (IOError, ValueError):
        return

    # حلقه برای مقادیر ممکن a
    # چون a < b < c و a+b+c=n است، پس a باید کمتر از n/3 باشد
    for a in range(1, n // 3 + 1):
        # با استفاده از فرمول‌های استخراج شده از معادلات، b را محاسبه می‌کنیم
        # a^2 + b^2 = c^2  و a + b + c = n
        # => b = n * (n - 2*a) / (2 * (n - a))
        numerator = n * (n - 2 * a)
        denominator = 2 * (n - a)

        # اگر صورت بر مخرج بخش‌پذیر بود، یک b صحیح پیدا کرده‌ایم
        if numerator % denominator == 0:
            b = numerator // denominator
            c = n - a - b
            
            # چک می‌کنیم که آیا شرایط a<b<c و فیثاغورثی برقرار است
            if a < b < c and a*a + b*b == c*c:
                print(a, b, c)
                return # با پیدا شدن اولین جواب، خارج می‌شویم
    
    # اگر حلقه تمام شد و جوابی پیدا نشد
    print("Impossible")

# برای اجرا، این تابع را فراخوانی کنید
find_pythagorean_triple_with_sum_n()