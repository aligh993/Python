# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import re

def simple_spell_checker():
    """
    Finds "misspelled" words in a text.
    Based on the sample output, a word is considered misspelled if:
    1. It is NOT an abbreviation (i.e., not all-caps).
    2. It contains NO vowels from the set {'a', 'e', 'i', 'o', 'u'}.
    """
    try:
        # خواندن کل ورودی (که ممکن است چند خط باشد)
        text = ""
        while True:
            line = input()
            text += line + " "
    except EOFError:
        pass

    # با استفاده از عبارات باقاعده، کلمات را استخراج می‌کنیم
    words = re.findall(r'[a-zA-Z]+', text)
    vowels = "aeiou"
    misspelled_words = []

    for word in words:
        # شرط ۱: کلمه نباید مخفف (تماماً بزرگ) باشد
        if not word.isupper():
            # شرط ۲: کلمه نباید هیچ حرف صداداری داشته باشد
            has_vowel = False
            for char in word.lower():
                if char in vowels:
                    has_vowel = True
                    break
            if not has_vowel:
                misspelled_words.append(word)

    print(" ".join(misspelled_words))

# برای اجرا، این تابع را فراخوانی کنید
simple_spell_checker()