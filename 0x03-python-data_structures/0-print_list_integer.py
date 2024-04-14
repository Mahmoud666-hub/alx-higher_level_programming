#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        i = 0
        while i < len(my_list):
            if type(my_list[i]) == int:
                print("{}".format(my_list[i]))
            i += 1
