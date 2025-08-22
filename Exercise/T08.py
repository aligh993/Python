# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import math

def solve_quadratic_equation():
    """
    Solves the quadratic equation ax^2 + bx + c = 0.
    Handles cases where a=0.
    """
    try:
        a = float(input())
        b = float(input())
        c = float(input())
        # a, b, c = map(float, input().split())
    except (IOError, ValueError):
        return

    # حالت خاص: اگر a صفر باشد، معادله خطی است (bx + c = 0)
    if a == 0:
        if b != 0:
            root = -c / b
            print(f"{root:.3f}")
        else:
            # اگر a و b هر دو صفر باشند
            # اگر c هم صفر باشد (0=0)، بی‌نهایت جواب دارد
            # اگر c غیرصفر باشد (c=0)، جواب ندارد
            if c != 0:
                print("IMPOSSIBLE")
            else:
                # مسئله حالت بی‌نهایت جواب را مشخص نکرده است
                # با توجه به ماهیت سوالات، این حالت معمولا در تست‌ها نمی‌آید
                pass 
        return

    # محاسبه دلتا (discriminant)
    delta = (b**2) - (4 * a * c)

    if delta < 0:
        # دلتای منفی: جواب حقیقی ندارد
        print("IMPOSSIBLE")
    elif delta == 0:
        # دلتای صفر: یک جواب مضاعف
        root = -b / (2 * a)
        print(f"{root:.3f}")
    else:
        # دلتای مثبت: دو جواب حقیقی متمایز
        sqrt_delta = math.sqrt(delta)
        root1 = (-b - sqrt_delta) / (2 * a)
        root2 = (-b + sqrt_delta) / (2 * a)
        
        # چاپ جواب‌ها به ترتیب صعودی
        if root1 < root2:
            print(f"{root1:.3f}")
            print(f"{root2:.3f}")
        else:
            print(f"{root2:.3f}")
            print(f"{root1:.3f}")

# برای اجرا، این تابع را فراخوانی کنید
solve_quadratic_equation()