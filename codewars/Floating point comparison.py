def get_pins(observed):
    x = {
        '0': '8',
        '1': ('2', '4'),
        '2': ('1', '3', '5'),
        '3': ('2', '6'),
        '4': ('1', '5', '7'),
        '5': ('2', '4', '6', '8'),
        '6': ('3', '5', '9'),
        '7': ('4', '8'),
        '8': ('5', '7', '9', '0'),
        '9': ('6', '8')
    }
    l = [observed]
    for i in observed:
        st = observed
        print("i-",i)
        for v in x[i]:
            print('x[i]=',x[i],'v=',v,'i=',i)
            st = observed
            print("st=",st)
            st=st.replace(i,v)
            print('st==',st)
            l.append(st)
            print('l=',l)
        pass

    return l


if __name__ == "__main__":
    print(get_pins('8'))
    print(['5', '7', '8', '9', '0'])
    print(get_pins('11'))
    print(["11", "22", "44", "12", "21", "14", "41", "24", "42"])

    # assert observed([]) == 'no one likes this'
    # assert observed(['Peter']) == 'Peter likes this'
    # assert likes(['Jacob', 'Alex']) == 'Jacob and Alex like this'
    # assert likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this'
    # assert likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this'
