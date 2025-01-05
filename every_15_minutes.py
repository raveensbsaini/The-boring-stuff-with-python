def func():
    minutes = ["00","15","30","45"]
    hours = ["12"] + [str(i) for i in range(1,12)]
    for hour in hours:
        for min in minutes:
            print(f"{hour}:{min}am")

    for hour in hours:
            for min in minutes:
                print(f"{hour}:{min}pm")
        
        
    return None
func()

