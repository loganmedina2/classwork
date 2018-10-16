def float_to_int(float_list):
    int_list = []
    for f in float_list:
        int_list.append(int(f))
        return int_list

def string_sandbox(string_list):
    cap_list = []
    for s in string_list:
        cap_list.append(s[:1].upper() + s[1:])
    return " ".join(cap_list)

if __name__ == '__main__':
    floats = [float(i) for i in range(100)]
    ints = (float_to_int(floats))
    print(ints)
    strings = ['s' + str(f) for f in floats]
    #which is equivalent to
    #strings = []
    #for f in floats:
     #   strings.append('s' + str(f))
    print(strings)
    print(string_sandbox(strings))
    s = "a string"
   # s = (s.upper())
   # print(s)
    #print(s[:1].upper() + s[1:])
