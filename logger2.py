def logger(filename):
    def decorator(func):
        def war(*args,**kwargs):
            result = func(*args,**kwargs)
            with open(filename, 'a') as f:
                f.write(str(result)+'\n')
            return result
        return war
    return decorator

@logger('new_log.txt')
def summator(list):
    return sum(list)
summator([1,2,3,4,5,6,7,8,9,10])
with open('new_log.txt','r') as f:
    print(f.read())


