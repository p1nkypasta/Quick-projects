from time import sleep

#input your own time limit
print('input time limit (in seconds)')               
time_limit = int(input('---> '))

x = 1
while x <= time_limit:
        sleep(1)
        print(x)
        x += 1
print('done')