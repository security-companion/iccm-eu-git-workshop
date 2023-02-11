# This program reads the content of all txt-files in the folder input-files and adds them one by one

import os

def  main():

    total_number = 0

    for file_name in os.listdir("input-files"):
        if file_name.endswith(".txt"):
            print("Reading content of file {}".format(file_name))

            f = open("./input-files/" + file_name, "r")
            lines = f.readlines()

            for line in lines:
                print(line, end="")
                total_number = total_number + int(line)
            print("\n")

    print("\n\n" + "*" * 60)
    print("Summary of all numbers in all files is: {}".format(total_number))
    print("*" * 60 + "\n")

if  __name__ == "__main__":
    main()
