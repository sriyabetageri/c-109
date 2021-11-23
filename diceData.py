import random
import statistics
import plotly.figure_factory  as ff

diceresult = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult.append(dice1+dice2)

mean = sum(diceresult)/len(diceresult)
median = statistics.median(diceresult)
mode = statistics.mode(diceresult)
std_dev = statistics.stdev(diceresult)
print(mean)
print(median)
print(mode)
print(std_dev)

fig = ff.create_distplot([diceresult],["result"],show_hist=False)

fstd_start,fstd_end = mean-std_dev, mean + std_dev
sstd_start,sstd_end = mean-(2*std_dev), mean + (2*std_dev)
tstd_start,tstd_end = mean-(3*std_dev), mean + (3*std_dev)



list_of_data_within_1_std_deviation = [result for result in diceresult if result > fstd_start and result < fstd_end]
list_of_data_within_2_std_deviation = [result for result in diceresult if result > sstd_start and result < sstd_end]
list_of_data_within_3_std_deviation = [result for result in diceresult if result > tstd_start and result < tstd_end]


print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(diceresult)))

print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(diceresult)))


print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(diceresult)))








