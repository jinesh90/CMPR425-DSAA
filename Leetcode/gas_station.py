"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next
(i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once
 in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

"""


def brute_force_sol(gas, cost):
    n = len(gas)
    for i in range(n):
        tank = 0
        possible = True
        for j in range(i, n+i):
            station_index =j % n
            tank = tank + gas[station_index] - cost[station_index]
            if tank < 0:
                possible = False
                break
        if possible:
            return i
    return -1


def optimal_solution(gas, cost):
    n = len(gas)
    # taking diff at every gas station
    diff = [gas[i] - cost[i] for i in range(n)]
    #print(diff)
    diff_total = sum(diff)

    # now of total is negative no solution
    if diff_total < 0:
        return -1
    else:
        start, tank = 0, 0
        for i in range(n):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start


print(optimal_solution([1,2,3,4,5], [3,4,5,1,2]))


