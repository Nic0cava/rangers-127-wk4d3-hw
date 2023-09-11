import time

start = time.time()

# runtime: 7.5 avg
def number_to_string(num):  # the reason this code runs slower is becasue it is using a method,
    string = str(num)       # tiem complexity is a bit worse due to the creation of a new variable 
    return string
    
# runtime: 6.5  avg
def number_to_string(num): # this code runs faster becasue the variable is not getting passed through a method
    return f"{num}"


end = time.time()
print(end - start)