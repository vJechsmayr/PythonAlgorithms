def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    sum1, rounds, temp = sum(range(1, num_people + 1)), 0, candies
    # 1. get the number of rounds that will go through the array
    while temp > 0:
        temp -= sum1 + rounds * num_people ** 2
        rounds += 1
    rounds -= 1
    result = [0] * num_people
    # 2. add up the number until right before the final round
    if rounds > 0:
        for i in range(1, num_people + 1):
            result[i - 1] = (2 * i + (rounds - 1) * num_people) * rounds // 2
            candies -= result[i - 1]
    base_num = num_people * rounds
    # 3. add the final round of numbers
    for i in range(1, num_people + 1):
        if candies <= base_num + i:
            result[i - 1] += candies
            break
        else:
            result[i - 1] += base_num + i
            candies -= base_num + i
    return result