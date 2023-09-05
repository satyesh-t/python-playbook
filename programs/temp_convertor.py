"""
    C TO F
    F to C
"""


def to_celicus(fht):
    cel = (fht - 32) *5/ 9
    return cel


def to_fht(cel):
    fht = ((cel * 9) / 5) + 32
    return fht


def convert(temp, type):
    print(f"type is {type} and temp is {temp}")
    temp = float(temp)
    if type == 'C':
        return to_fht(temp)
    elif type == 'F':
        return to_celicus(temp)
    else:
        return "Invalid Temp Type"


input_temp = input("Enter the Temp")
input_type = input_temp[-1]
input_temp = input_temp[:len(input_temp) - 1]
print(f"output:{convert(input_temp, input_type)}")
