from itertools import combinations

def find_distance(pair):
    pass

def find_combos(drivers, passengers):
    if len(drivers) != len(passengers):
        return None
    passenger_driver_combos = [(driver, passenger) for driver in drivers for passenger in passengers]
    solutions = list(combinations(passenger_driver_combos, len(drivers)))
    pop_list = []
    for i in range(len(solutions)):
        test_list = []
        for pair in solutions[i]:
            for item in pair:
                test_list.append(item)
        for driver in drivers:
            if test_list.count(driver) != 1:
                pop_list.append(i)
        for passenger in passengers:
            if test_list.count(passenger) != 1:
                pop_list.append(i)
    pop_list = list(set(pop_list))
    pop_list.sort(reverse=True)
    for i in pop_list:
        solutions.pop(i)
    return solutions