def brutal(apples: list, days: list):
    day = 0
    apple_dict = dict()
    # for i in range(len(apples)):
    counter = 0
    while (len(apples) - counter > 0) or apple_dict:
        if apple_dict:
            apple_dict = {(k - 1): v for k, v in apple_dict.items() if k > 0}
        if counter < len(apples):
            if apples[counter] > 0:
                apple_dict.update({days[counter]: apples[counter]})

        apple_dict_ = {k: v for k, v in apple_dict.items() if k > 0 and v > 0}
        if apple_dict_:
            chosen_date = min(apple_dict_.keys())
            apple_dict[chosen_date] = apple_dict_[chosen_date] - 1
            print(apple_dict)
            day += 1
        counter += 1
    return day


if __name__ == "__main__":
    # apples = [3, 0, 0, 0, 0, 2]
    # days = [3, 0, 0, 0, 0, 2]
    apples = [1, 2, 3, 5, 2]
    days = [3, 2, 1, 4, 2]

    day_to_eat = brutal(apples, days)
    print(day_to_eat)
