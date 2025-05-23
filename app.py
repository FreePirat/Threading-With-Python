import threading 
import time

# Creating a dictionary of results, as threads cannot print their results

results = {}

def longSquare(num, results):
  time.sleep(1)
  results[num] = num**2

# Threading makes this, otherwise long process, go by much faster by connecting
# Two threads of data

t1 = threading.Thread(target=longSquare, args=(1, results))
t2 = threading.Thread(target=longSquare, args=(2, results))

t1.start()
t2.start()

t1.join()
t2.join()

print(results) # So, by printing results, you get to see that the data 
# Both come from seperate threads which halve the wait time and both share
# data

# A way of simplifying threads would look like this

# threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range (0, 10)]
# [t.start() for t in threads]
# [t.join() for t in threads]
# print(results)