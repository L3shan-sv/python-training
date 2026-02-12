
def fizzbuzz(n):
    result = []

    for i in range(1, n+1):
        if i % 15 == 0:            # divisible by both 3 and 5 first
            result.append("FizzBuzz")
        elif i % 3 == 0:           # divisible by 3
            result.append("Fizz")
        elif i % 5 == 0:           # divisible by 5
            result.append("Buzz")
        else:                      # everything else
            result.append(i)

    return result


# Test it
print(fizzbuzz(15))
