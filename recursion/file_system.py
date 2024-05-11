import os

def file_system(path: str):
    total = os.path.getsize(path)
    if(os.path.isdir(path)):
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            total += file_system(child_path)
    
    print("{0:<7}".format(total), path)
    return total

file_system(r"D:\Learning")