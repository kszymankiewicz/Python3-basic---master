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
    
start = time.perf_counter()
print(sum_to(25555))
print(finish_timer(start))

start = time.perf_counter()
print(sum_to2(25555))
print(finish_timer(start))

start = time.perf_counter()
print(sum_to3(25555))
print(finish_timer(start))

start = time.perf_counter()
print(sum_to4(25555))
print(finish_timer(start))

start = time.perf_counter()
print(sum_to5(25555))
print(finish_timer(start))