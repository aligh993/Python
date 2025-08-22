# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def fruits(fruit_list):
    f_list = []
    for i in fruit_list:
        if i['shape'] == 'sphere' and 300 <= i['mass'] <= 600 and 100 <= i['volume'] <= 500:
            f_list.append(i['name'])

    print({x: f_list.count(x) for x in f_list})
    return {x: f_list.count(x) for x in f_list}
