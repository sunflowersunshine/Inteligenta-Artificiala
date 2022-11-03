import numpy
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]


# Viteza medie
x = numpy.mean(speed)
print("Viteza media e unei masini:", x)


# Valoarea mediana
y = numpy.median(speed)
print("Valoarea mediana:", y)

# Valoarea Mode
z = stats.mode(speed, keepdims=False)
print("Valoarea mediana:", z)

# Abaterea standard
speed = [86, 87, 88, 86, 87, 85, 86]
w = numpy.std(speed)
print("Abaterea standard:", w)

# Deviatia standard
speed = [32, 111, 138, 28, 59, 77, 97]
r = numpy.var(speed)
print("Deaviatia standard:", w)

# Gasirea percentilei
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39,
        80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
t = numpy.percentile(ages, 75)
print("Gasirea percentilei", t)

# crearea unei matrici ce contine 250 de elemente flotante aleatorii intre 0 si 5
x = numpy.random.uniform(0, 5, 250)
print(x)
