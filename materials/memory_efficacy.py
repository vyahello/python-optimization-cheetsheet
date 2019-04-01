import sys
import cProfile


generator_container = (num * 3 for num in range(10000000) if num % 6 == 0 or num % 7 == 0)
print(sys.getsizeof(generator_container))

list_container = [num * 3 for num in range(10000000) if num % 6 == 0 or num % 7 == 0]
print(sys.getsizeof(list_container))

print(cProfile.run('sum(generator_container)'))
print(cProfile.run('sum(list_container)'))
