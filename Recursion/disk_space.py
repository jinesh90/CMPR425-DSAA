"""
calculating disk space for given path recursive way.
"""
import os


def disk_size(path):
    total_size = os.path.getsize(path)
    # check if path is directory
    if os.path.isdir(path):
        for files in os.listdir(path):
            childpath = os.path.join(path, files)
            total_size += disk_size(childpath)
    print("{} {}".format(total_size, path))
    return total_size


print(disk_size("/home/jinesh/Desktop/AIML"))