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

    print(count_pillars(targetSum-1, targetSum))
    sys.exit(0)

#  Let's define function that takes number of blocks as referance
#  and number of all blocks - 1 (since we cannot build single tower)
def count_pillars(n, target):
    #  if we depleted out sum, it means we have it and return 1 to increment counter
    if target == 0:
        return 1
    #  if we don't have more elements return 0
    if n == 0:
        return 0
    #  if next item is greater than what we have left up to our sum,
    #  go to next item
    if n > target:
        return count_pillars(n-1, target)
    else:
        # now we go deeper into recurson with each number in tree - included and excluded, then add number of sums together
        return count_pillars(n-1, target) + count_pillars(n-1, target - n)


main()
