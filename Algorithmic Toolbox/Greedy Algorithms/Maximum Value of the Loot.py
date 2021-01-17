n, total_weigth = list(map(int, input().split()))
values = list()
weights = list()
for i in range(n):
    x = list(map(int, input().split()))
    values.append(x[0])
    weights.append(x[1])
    
vperw = list()
for i in range(len(values)):
    vperw.append(values[i] / weights[i])

profit = 0.0

while total_weigth > 0:
    max_vperw_index = vperw.index(max(vperw))
    if weights[max_vperw_index] > total_weigth:
        profit += (total_weigth / weights[max_vperw_index]) * values[max_vperw_index]
        total_weigth = 0
    else:
        total_weigth -= weights[max_vperw_index]
        profit += values[max_vperw_index]
    vperw[max_vperw_index] = -1
    
print("{0:.4f}".format(profit))
