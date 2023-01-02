
# importing libraries needed
import random


def montecarlo(n):
    r1 = 0
    r2 = 0
    r3 = 0
    total = []
    for x in range(n):

        # assign values to tasks A,B,C
        a = random.randint(8, 12)
        b = random.randint(10, 14)
        c = random.randint(12, 16)

        # calculating the total days
        total_days = a + b + c
        total.append(total_days)

        # checking which range the value belongs to
        if total_days in range(30, 36):
            r1 += 1

        elif total_days in range(36, 39):
            r2 += 1

        elif total_days in range(39, 42):
            r3 += 1

    # calculatin the probability of each range
    r1 = (r1 / n) * 100
    r2 = (r2 / n) * 100
    r3 = (r3 / n) * 100
    return (print("\n30-35={}% \n36-38={}% \n39-42={}% \n\nGenerated day={}".format(r1, r2, r3, total)))


# getting the input from the user
iterative_no = int(input("\nEnter the number of iterations that you want : "))
montecarlo(iterative_no)
