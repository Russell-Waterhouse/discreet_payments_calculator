default_inflation_rate = 0.03


def future_to_present(future_value, interest_rate, periods, inflation_rate=default_inflation_rate):
    real_interest_rate = get_real_interest_rate(inflation_rate, interest_rate)
    denominator = pow(1 + real_interest_rate, periods)
    if denominator == 0:
        return 0
    return future_value / denominator


def get_real_interest_rate(inflation_rate, interest_rate):
    real_interest_rate = interest_rate
    if inflation_rate != 0:
        real_interest_rate = ((1 + interest_rate) / (1 + inflation_rate)) - 1
    return real_interest_rate


def present_to_future(present_value, interest_rate, periods, inflation_rate=default_inflation_rate):
    real_interest_rate = get_real_interest_rate(inflation_rate, interest_rate)
    return present_value * pow(1 + real_interest_rate, periods)


def annuity_to_future(annuity, interest_rate, periods, inflation_rate=default_inflation_rate):
    # TODO: finish when I have this equation
    return -1


def future_to_annuity(future, interest_rate, periods, inflation_rate=default_inflation_rate):
    # TODO: finish when I have this equation
    return -1


def annuity_to_present(annuity, interest_rate, periods, inflation_rate=default_inflation_rate):
    # TODO: finish when I have this equation
    return -1


def present_to_annuity(present, interest_rate, periods, inflation_rate=default_inflation_rate):
    # TODO: finish when I have this equation
    return -1


def annuity_to_geometric(annuity, interest_rate, periods, inflation_rate=default_inflation_rate):
    # TODO: finish when I have this equation
    return -1
