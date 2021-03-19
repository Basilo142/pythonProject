class Value:
    # print('class Value:')
    def __get__(self, obj, obj_type):
        # print('def __get__(self, obj, obj_type):')
        return self.sum

    def __set__(self, obj, sum):
        # print('def __set__(self, obj, sum):')
        self.sum = sum - sum * obj.commission


# class Account:
#     print("class Account:")
#     amount = Value()
#     print("amount = Value()")
#
#     def __init__(self, commission):
#         print('def __init__(self, commission')
#         self.commission = commission
#
# print("_ до_ nwe = Account(0.1)")
# nwe = Account(0.1)
# print("_ после_ nwe = Account(0.1)")
# nwe.amount = 100
# print("nwe.amount = 100)")
# print(nwe.amount)
