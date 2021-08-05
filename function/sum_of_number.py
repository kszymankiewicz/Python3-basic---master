import time
def sum_to(number):
    sum = 0
    
    for number in range(1,number+1):
        sum = sum + number
        
    return sum

def sum_to2(number):
    return sum([number for number in range(1,number+1)])

def sum_to3(number):
    return sum({number for number in range(1,number+1)})

def sum_to4(number):
    return sum((number for number in range(1,number+1)))

def sum_to5(number):
    return (1 + number) / 2 * number

def finish_timer(start):
    end = time.perf_counter()
    return end-start

def function_performance(func,arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end-start

print(function_performance(sum_to,500000))
print(function_performance(sum_to2,500000))
print(function_performance(sum_to3,500000))
print(function_performance(sum_to4,500000))
print(function_performance(sum_to5,500000))