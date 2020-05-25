def kidsWithCandies(candies, extraCandies):
    most = max(candies)

    return [x + extraCandies >= most for x in candies]