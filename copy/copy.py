

"""
Usage: python3 copy.py fileFrom fileTo

"""
import os

chucksize = 1024


def copyFile(source, destination, chucksize=chucksize):
    source_abs = os.path.abspath(source)
    destination_abs = os.path.abspath(destination)

    if not os.path.isfile(source_abs):                          # check file exists
        print(f"..{source_abs} not found")

    if not os.path.isdir(destination_abs):                       # check destination exist
        os.mkdir(destination_abs)                                # if does not create new dir

    destination_address = destination_abs + os.sep + source

    with open(source_abs, 'rb') as source_file, open(destination_address, "wb") as destination_file:
        print(source_file)

        """
        Done:
            - have tested to insure source exists and if destination exist(else build it)
            - opened files with context manager in binary mode
            - created a new file

        TODO:
            - create loop to read chucks from source and write to destination
            
        """












if __name__ == "__main__":
    import sys

    copyFile(sys.argv[1], sys.argv[2])
