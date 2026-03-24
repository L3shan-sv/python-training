numbers = [1, 2, 3, 4, 5, 6]
# Sum of even numbers: 2 + 4 + 6 = 12
# Count of odd numbers: 1, 3, 5 → 3
# Output: (12, 3)

def number_count(numbers):
    even_total=0
    odd_toatal=0
    
    for x in numbers:
        if x %2==0:
            print ("Number is even")
            even_total= x+x
        elif x%2 !=:
            print("Odd")
            odd_count= x+x    
            