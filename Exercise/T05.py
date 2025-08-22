# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def find_next_power_of_two():
    """
    Finds the smallest power of 2 that is strictly greater than n.
    """
    try:
        n = int(input())
    except (IOError, ValueError):
        return
        
    power_of_2 = 1
    # تا زمانی که توان دو کوچکتر یا مساوی n است، آن را در ۲ ضرب کن
    while power_of_2 <= n:
        power_of_2 *= 2
    
    print(power_of_2)

# برای اجرا، این تابع را فراخوانی کنید
find_next_power_of_two()