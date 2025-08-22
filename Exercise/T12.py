# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def virus_file_renamer():
    """
    Simulates a file renaming virus by prepending "copy of " k times
    to a given filename.
    """
    try:
        parts = input().split()
        k = int(parts[0])
        filename = parts[1]
        
        # عبارت "copy of " را k بار تکرار کرده و به نام فایل می‌چسبانیم
        prefix = "copy of " * k
        
        print(prefix + filename)
    except (IOError, ValueError, IndexError):
        return

# برای اجرا، این تابع را فراخوانی کنید
virus_file_renamer()