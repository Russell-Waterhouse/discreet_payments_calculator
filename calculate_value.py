def future_to_present(future_value, interest_rate, periods):
    denominator = pow(1 + interest_rate, periods)
    if denominator == 0:
        return None
    return future_value / denominator


def present_to_future(present_value, interest_rate, periods):
    return present_value * pow(1 + interest_rate, periods)


def present_to_future_inflation(present_value, interest_rate, periods, inflation_rate):
    # TODO: finish when I have this equation
    return -1


def future_to_present_inflation(future_value, interest_rate, periods, inflation_rate):
    # TODO: finish when I have this equation
    return -1


def annuity_to_present():
    # TODO: finish when I have this equation
    return -1
