l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 24, 23, 25, 24, 27, 30]
print(l)


def print_words(s):
    s[:] = [i//2 for i in s if i % 2 == 0]


print('l1=', l)

if __name__ == "__main__":
    print_words(l)


print('l2=', l)


# *****************************************************************
# f = open("r.txt")
# foo = f.readline()
#
# if os.fork() == 0:
#     foo = f.readline()
#     print("child:", foo)
# else:
#     foo = f.readline()
#     print("parent:", foo)

# ***************************************************************************************
# foo = "bar"
#
# if os.fork() == 0:
#     foo = "baz"
#     print("child:", foo)
# else:
#     print("parent:", foo)
#     os.wait()

# *****************************************************************************************
#
# pid = os.fork()
# if pid == 0:
#     while True:
#         print("child:", os.getpid())
#         time.sleep(5)
# else:
#     print("parent:", os.getpid())
#     os.wait()
#
# *****************************************************************************************
#
# while True:
#     print ("pid = ", pid,"time", time.time())
#     time.sleep(2)