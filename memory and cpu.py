import psutil
import time
# print(psutil.cpu_times())
# print(psutil.cpu_stats())
# for x in range(3):
#     print()

# print(psutil.getloadavg())

def monitor():
    i = 0
    avgv = 0
    avgs = 0
    vm = []
    sm = []
    j=0
    while True:
        if (i==5):
            vm.pop(0)
            sm.pop(0)
            i=0
        else:
            pass
        vm.append(psutil.virtual_memory().percent)
        sm.append(psutil.swap_memory().percent)
        for x in range(1,len(vm)):
            avgv =avgv + abs(vm[x] - vm[x-1])
            avgs =avgs + abs(sm[x] - sm[x-1])
        avgv = avgv/len(vm)
        avgs = avgs/len(sm)
        
        if j >2:
            if abs(vm[-1]-vm[-2]) >= 2*avgv or abs(sm[-1] - sm[-2]) >= 2*avgs:
                # print(2*avgv)
                if psutil.cpu_percent(interval=1) >=95.0:
                    print("Possiblity Of server hang is high")
                else:
                    print("Running smoothly")

            else:
                print("Running smoothly")
        else:
            print("ELSE")
        i = i+1
        j = j+1
        time.sleep(1)