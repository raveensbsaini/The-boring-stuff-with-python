def convertToFahrenheit(temp):
    return (temp * (9/5)) + 32

def convertToCelsius(temp):
    return (temp -32)*(5/9)

assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001
