import functools
def logger(func):
    @functools.wraps(func)
    def wra(*args,**kwargs):
        result=func(*args, **kwargs)
        with open('logg.txt', 'a') as f:
            f.write(str(result)+'\n')
        return result
    return wra




@logger
def summator (num_list):
    return sum(num_list)

print(summator([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21, 22, 34]))
print(summator.__name__)