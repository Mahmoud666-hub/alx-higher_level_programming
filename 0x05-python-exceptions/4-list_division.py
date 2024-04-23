#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lst = []
    for i in range(list_length):
        try:
            lst.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            lst.append(0)
        except TypeError:
            print("wrong type")
            lst.append(0)
        except ZeroDivisionError:
            print("division by 0")
            lst.append(0)
        finally:
            if i == list_length - 1:
                return lst
