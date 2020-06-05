# Enter your code here. Read input from STDIN. Print output to STDOUT


Score1 = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
Score2 = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]


def pearson_coefficient(Score1, Score2):
    "Calculating the person coefficient"
    m1 = sum(Score1) / len(Score1)
    m2 = sum(Score2) / len(Score1)

    Score_1 = [x - m1 for x in Score1]
    Score_2 = [x - m2 for x in Score2]

    n1 = sum([x * y for x, y in zip(Score_1, Score_2)])

    Score1 = sum([(x - m1) ** 2 for x in Score1])
    Score2 = sum([(x - m2) ** 2 for x in Score2])

    n2 = (Score1 ** (1 / 2)) * (Score2 ** (1 / 2))

    r = n1 / n2
    return r


print(f"Pearson coefficient is {round(pearson_coefficient(Score1,Score2), 3)}")


def get_slope_of_the_line(Score1, Score2):
    mean_x = sum(Score1) / len(Score1)
    mean_y = sum(Score2) / len(Score1)

    X = [mean_x - x for x in Score1]
    Y = [mean_y - y for y in Score2]

    slope = sum([a * b for a, b in zip(X, Y)]) / sum([a * a for a in X])
    return slope


print(f"Slope of the line is {round(get_slope_of_the_line(Score1,Score2), 3)}")
