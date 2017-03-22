import random
random.seed(1)
def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors

    mean_values = []
    for i in range(n):
        temp = x[i: i+width]
        sum_= 0
        for elm in temp:
            sum_+= elm
        mean_values.append(sum_ / width)
    return mean_values

R = 1000
x = [random.uniform(0,1) for i in range(R)]
print(x) 

Y = list([]) 
Y.append(x)
for n_neighbors in range(1 , 10):
    y = moving_window_average(x , n_neighbors)
    Y.append(y)

print(Y)