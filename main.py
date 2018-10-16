def float_to_int(float_list):
    int_list = []
    for f in float_list:
        int_list.append(int(f))
        return int_list
if __name__ == '__main__':
    floats = [float(i) for i in range(100)]
    print(float_to_int(float))
