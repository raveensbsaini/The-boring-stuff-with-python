def getCostOfCoffee(numberOfCoffees,pricePerCoffee):
    if numberOfCoffees <= 8:
        return numberOfCoffees * pricePerCoffee
    else:
        block_price = 8 * pricePerCoffee
        number_of_blocks = numberOfCoffees // 9
        left = numberOfCoffees - (number_of_blocks * 9)
        return (block_price * number_of_blocks) + (left * pricePerCoffee)

assert getCostOfCoffee(7, 2.50) == 17.50
assert getCostOfCoffee(8, 2.50) == 20
assert getCostOfCoffee(9, 2.50) == 20
assert getCostOfCoffee(10, 2.50) == 22.50
for i in range(1, 4):
    assert getCostOfCoffee(0, i) == 0
    assert getCostOfCoffee(8, i) == 8 * i
    assert getCostOfCoffee(9, i) == 8 * i
    assert getCostOfCoffee(18, i) == 16 * i
    assert getCostOfCoffee(19, i) == 17 * i
    assert getCostOfCoffee(30, i) == 27 * i
