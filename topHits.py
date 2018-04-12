#!/bin/python
#this Code is Going to find top 10 IPs
#which have the highest hit rate
if __name__ == '__main__':
    #List Variables
    lst = []
    pairs = {}
    sortedPairs = []
    #Reading The Log File
    with open('/var/log/httpd/access.log') as f:
        lst = f.read().splitlines()
    mySet = list(set(lst))
    for i in range(len(mySet)):
        pairs[mySet[i]] = lst.count(mySet[i])
    sortedPairs = list(sorted(pairs.items(), key=lambda x:x[1], reverse=True))
    for j in range(10):
        print(str(sortedPairs[j][0]) + ":" + str(sortedPairs[j][1]))
