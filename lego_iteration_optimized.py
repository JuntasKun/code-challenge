import sys


def main():
    while True:
        try:
            targetSum = int(input("Enter number of lego blocks: "))
            if targetSum < 1:
                raise ValueError
        except ValueError:
            print("Enter valid number of lego blocks")
        except KeyboardInterrupt:
            sys.exit(1)
        else:
            break

    count_pillars(targetSum)
    sys.exit(0)


def count_pillars(targetSum):
    # First of all, let's create a list to store our counts of sums in it
    row = [0 for i in range(targetSum + 1)]
    # First element of the list will be initialized to 0 since with 0 elements we can create 1 sum of 0
    row[0] = 1
    # Next let's set i lor loop to be equal to 1 and it will represent one as lowest number as well
    i = 1
    while i < targetSum:  # We nest two loops to go from 1 to sum
        j = targetSum
        while j >= i:     # And sum to i
            # Now we add number of sums up to j without ith element and number of sums that add up to j - i with ith element
            row[j] = row[j] + row[j - i]
            j -= 1
        i += 1

    print(f"Number of combinations: {row[targetSum]}")


main()
