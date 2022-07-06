import collections
user_input = input("напиши числа: ")
n = int(input("на сколько сдвигов хотите: "))
a_list = collections.deque((list(user_input)))
a_list.rotate(n)
result = list(a_list)
print(result)