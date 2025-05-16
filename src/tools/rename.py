import os

def batch_rename(folder, rule_func):
    for filename in os.listdir(folder):
        old_path = os.path.join(folder, filename)
        if os.path.isfile(old_path):
            new_name = rule_func(filename)
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)