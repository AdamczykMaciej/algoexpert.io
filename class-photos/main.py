# Class Photos
#
# Source: https://www.algoexpert.io/questions/class-photos
#
# It's photo-day at the local school, and you're the photographer. Students
# are split into red-shirt and blue-shirt groups (equal sized) and arranged
# in two rows for a photo. The following rules apply:
#   - All students wearing red shirts must be in the same row.
#   - All students wearing blue shirts must be in the same row.
#   - Each student in the back row must be strictly taller than the student
#     directly in front of them in the front row.
#
# You're given two non-empty arrays of positive integers (of equal length)
# representing the heights of all red-shirt and blue-shirt students. Return
# whether or not a class photo that follows the rules can be taken.
#
# Sample Input:
#   redShirtHeights  = [5, 8, 1, 3, 4]
#   blueShirtHeights = [6, 9, 2, 4, 5]
#
# Sample Output:
#   True


# Solution 1: Check both arrangements with flag
# Time: O(n log n) | Space: O(1)
#
# Sort both ascending, then try arrangement A (blue in back, every blue must
# be strictly taller than its red). If that fails, try arrangement B (red in
# back). The flag-and-break style keeps the two passes independent.
def classPhotos_flag(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    # are red < blue
    # are blue < red
    good = 0
    for i in range(len(redShirtHeights)):
        if redShirtHeights[i] < blueShirtHeights[i]:
            good = 1
        else:
            good = 0
            break

    if good:
        return True
    else:
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] > blueShirtHeights[i]:
                good = 1
            else:
                good = 0
                break

    if good:
        return True
    return False


# Solution 2: Pick back row from tallest, single pass
# Time: O(n log n) | Space: O(1)
#
# Sort both descending. The back row must contain the tallest student, so
# compare the two tallest values to decide which group is back. From there,
# at every index the back student must be strictly taller than the front;
# a single <= violation rules the arrangement out.
def classPhotos_canonical(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    tallestRed = redShirtHeights[0]
    tallestBlue = blueShirtHeights[0]
    # are red < blue
    # are blue < red
    for i in range(len(redShirtHeights)):
        if tallestBlue > tallestRed:
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
        else:
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False

    return True


# Solution 3: Pick back row once, zip-pair the rows
# Time: O(n log n) | Space: O(1)
#
# Same idea as solution 2 but lifts the back-row decision out of the loop.
# Sort descending, name back/front explicitly, then walk both rows in
# lockstep with zip — any pair where back <= front fails.
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    if redShirtHeights[0] > blueShirtHeights[0]:
        backRow, frontRow = redShirtHeights, blueShirtHeights
    else:
        backRow, frontRow = blueShirtHeights, redShirtHeights

    for back, front in zip(backRow, frontRow):
        if back <= front:
            return False
    return True
