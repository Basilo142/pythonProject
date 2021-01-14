def zero():
    pass
def one():
    pass

def two():
    pass
def three():
    pass
def four():
    pass
def five():
    print(5)
def six():
    pass

def seven():
    print(7)
def eight():
    pass
def nine():
    pass

def plus():
    pass
def minus():
    pass

def times():
    print("+")
def divided_by():
    pass


if __name__ == '__main__':
    print("Example:")
    print(seven(times(five())))

    #some test cases for you...
    assert wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    assert wave("codewars") == ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
    assert wave("") == []
    assert wave("two words") == ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
    # assert alphabet_position(70304) == '70000 + 300 + 4'
    # ven_index([20, 10, 30, 10, 10, 15, 35]) == 3
    # assert find_even_index([20, 10, -80, 10, 10, 15, 35]) == 0
    # assert find_even_index([10, -80, 10, 10, 15, 35, 20]) == 6
    # assert find_even_index(list(range(1, 100))) == -1
    # assert find_even_index([0, 0, 0, 0, 0]) == 0
    # assert find_even_index([-1, -2, -3, -4, -3, -2, -1]) == 3
    # assert find_even_index(list(range(-100, -1))) == -1