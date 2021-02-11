def int32_to_ip(int32):
    s = "{0:b}".format(int32)
    print(s)
    # print(bi)
    return s


if __name__ == "__main__":
    print(int32_to_ip(2154959208))
    print("128.114.17.104")


    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"
    # assert approx_equals(1456.3652, 1456.3641) == False
    # assert approx_equals(-1.234, -1.233999) == True
    # assert approx_equals(98.7655, 98.7654999) == True
    # assert approx_equals(-7.28495, -7.28596) == False
