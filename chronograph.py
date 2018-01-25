#! python3
#  秒表应用
import time
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1
try:
    while True:
        input()
        lapTime = round(time.time()-lastTime,2)
        totalTime = round(time.time()-startTime,2)
        print('Lap #%s: totalTime=%s (lapTime=%s),avgTime=%s' % (lapNum, totalTime, lapTime,totalTime/lapNum), end='')
        lapNum += 1
        lastTime = time.time()
except:
    print("\n Done")























