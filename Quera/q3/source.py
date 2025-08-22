# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def guess_generator_iterator(guess_generator, min_value, max_value, assumed_number):
    f_list = []
    count = 0

    for ex in guess_generator(min_value, max_value):
        if ex == assumed_number:
            f_list.append(ex)
        elif (ex <= min_value) or (ex >= max_value) or (ex == assumed_number):
            count += 1
            if count != 3:
                f_list.append('!')
            else:
                f_list.append('!!!')
                break
        else:
            f_list.append(ex)

    return f_list
