def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    
    wrapper.call_count = 0
    return wrapper
@call_counter
def greet(name):
    print(f"Hello, {name}!")

greet("Nikita")
greet("Fedya")
print(greet.call_count)  

@call_counter
def add(a, b):
    return a + b
result = add(5, 6)
print(result)
print(add.call_count)