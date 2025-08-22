# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

def check_registration_rules(**kwargs):
    valid = list()
    for name, password in kwargs.items():
        if name == "codecup" or name == "quera" or len(name) < 4 or len(password) < 6 or password.isdigit():
            continue
        else:
            valid.append(name)
    return valid
