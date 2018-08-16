import time
import sys


first_day = '20180611'
last_day = '20180722'
rate_up = 1.0075
shouxufei = 0.001*0.75
ganggan = 1.81
chushi_btc_amount = 1

if(len(sys.argv)>1):
    rate_up = float(sys.argv[1])
if(len(sys.argv)>2):
    shouxufei = float(sys.argv[2])
if(len(sys.argv)>4):
    first_day = sys.argv[3]
    last_day = sys.argv[4]

pre_dir = 'private/klines/BTCUSDT/{0}'
time_struct = time.strptime(first_day, '%Y%m%d')
ts_first_day = time.mktime(time_struct)
time_struct = time.strptime(last_day, '%Y%m%d')
ts_last_day = time.mktime(time_struct)
ts_index = ts_first_day
file_list = []
k_line = []
lines = []
while(ts_index <= ts_last_day):
    day_index = time.strftime('%Y%m%d', time.localtime(ts_index))
    file_list.append(day_index)
    ts_index = ts_index + 60*60*24

for val in file_list:
    file_day = pre_dir.format(val)
    with open(file_day, 'r') as f:
        for line in f.readlines():
            lines.append(line)

time_rate = -1
rate = -1
for line in lines:
    #print(line)
    time = line.split('\t')[0]
    high = float(line.split('\t')[2])
    low = float(line.split('\t')[3])
    if(high/low*1.0 > rate):
        rate = high/low*1.0
        time_rate = time

print(rate, time_rate)
