def fizzBuzzAnkit(upTo: int):
    for i in range(1, upTo + 1):
        if i % 3 == 0 and i % 5 == 0:
           print("FizzBuzz", end=" ")
        elif i % 3 == 0:
           print("Fizz", end=" ")
        elif i % 5 == 0:
          print("Fizz", end=" ")
        else:
            print(str(i), end=" ")


def fizzBuzz(upTo):
    for i in range(1,upTo+1):
        # print("i",i)
        run(i)
def run(i):
    divisible_by_3 = False
    divisible_by_5 = False
    if i //3 == i/3 :
        divisible_by_3 = True
    if i //5 == i/5 :
        divisible_by_5 = True
    # print("divisible_by_3",divisible_by_3)
    # print("divisible_by_5",divisible_by_5)
    if divisible_by_3 and  divisible_by_5:
        # print("both 3 and 5")
        print("FizzBuzz ",end="")
        return None
    if divisible_by_3 == False and divisible_by_5 == False:
        # print("both 3, and 5 none")
        print(i," ",end="")
        return None
    if (divisible_by_3 == False) and  divisible_by_5 == True:
        # print("only 3 false 5 true")

        print("Fizz ",end="")
        return
    if divisible_by_3 and  (divisible_by_5 == False):
        # print("only 3 true")
        print("Buzz ",end="")
        return
fizzBuzz(35)
print()
