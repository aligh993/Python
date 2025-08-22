# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def presidential_election_josephus():
    """
    Solves a variation of the Josephus problem.
    n people in a circle, every second person is eliminated.
    The recursive solution is based on the parity of n.
    """
    memo = {} # برای ذخیره نتایج و جلوگیری از محاسبات تکراری (Memoization)

    def solve_josephus(k):
        if k in memo:
            return memo[k]
        if k == 1:
            return 1
        
        # رابطه بازگشتی بر اساس زوج یا فرد بودن تعداد افراد
        if k % 2 == 0: # اگر زوج باشد
            result = 2 * solve_josephus(k // 2) - 1
        else: # اگر فرد باشد
            result = 2 * solve_josephus(k // 2) + 1
        
        memo[k] = result
        return result

    try:
        n = int(input())
        winner = solve_josephus(n)
        print(winner)
    except (IOError, ValueError):
        return

# برای اجرا، این تابع را فراخوانی کنید
presidential_election_josephus()