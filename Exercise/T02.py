# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def find_min_max_numbers():
    """
    Finds the smallest and largest numbers with a given length 'm'
    and sum of digits 's'.
    """
    try:
        m, s = map(int, input().split())
    except (IOError, ValueError):
        return

    # --- شرایط خاص ---
    # اگر مجموع ارقام صفر باشد، تنها در صورتی ممکن است که طول عدد ۱ باشد (عدد صفر)
    if s == 0:
        if m == 1:
            print("0 0")
        else:
            print("-1 -1")
        return

    # اگر مجموع ارقام خواسته شده از حداکثر مجموع ممکن (m * 9) بیشتر باشد، غیرممکن است
    if s > m * 9:
        print("-1 -1")
        return

    # --- ساخت بزرگترین عدد ---
    # برای بزرگترین عدد، ارقام بزرگتر (مثل ۹) باید در سمت چپ قرار گیرند
    largest_num_list = []
    temp_s_for_largest = s
    for _ in range(m):
        digit = min(9, temp_s_for_largest)
        largest_num_list.append(str(digit))
        temp_s_for_largest -= digit
    largest_num = "".join(largest_num_list)

    # --- ساخت کوچکترین عدد ---
    # برای کوچکترین عدد، از روی بزرگترین عدد ساخته شده کمک می‌گیریم و آن را معکوس می‌کنیم
    # این کار باعث می‌شود ارقام کوچکتر در سمت چپ قرار گیرند
    smallest_num_list = list(reversed(largest_num_list))
    
    # اگر رقم اول (سمت چپ) صفر بود، باید آن را با یک جابجا کنیم
    # برای این کار، اولین رقم غیرصفر از سمت چپ را پیدا کرده، یکی از آن کم می‌کنیم
    # و به رقم اول که صفر بود، یک واحد اضافه می‌کنیم (که می‌شود ۱)
    if smallest_num_list[0] == '0':
        smallest_num_list[0] = '1'
        for i in range(1, m):
            if smallest_num_list[i] != '0':
                smallest_num_list[i] = str(int(smallest_num_list[i]) - 1)
                break
                
    smallest_num = "".join(smallest_num_list)

    print(smallest_num, largest_num)

# برای اجرا، این تابع را فراخوانی کنید
find_min_max_numbers()