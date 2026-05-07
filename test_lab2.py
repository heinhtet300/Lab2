import temperature
import statistics
print("Test Lab2")


def test_minNmax():
    result = []
    testArr = [3,52,72,13,54,33]
    minMax = [min(testArr),max(testArr)]
    result = temperature.calc_min_max_temperature(testArr)
    assert(result == minMax)

def test_average():
    result = []
    testArr = [3,52,72,13,54,33]
    average = sum(testArr)/len(testArr)
    result = temperature.calc_average_temperature(testArr)
    assert(result == average)

def test_median():
    result = []
    testArr = [3,52,72,13,54,33,1]
    mean = statistics.median(testArr)
    result = temperature.calc_median_temperature(testArr)
    assert(result == mean)
    

    