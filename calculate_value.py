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


def future_to_annuity(future, interest_rate, periods, inflation_rate=default_inflation_rate):
    real_interest_rate = get_real_interest_rate(inflation_rate, interest_rate)
    denominator = pow(1+real_interest_rate, periods) - 1
    return real_interest_rate * future / denominator


def annuity_to_future(annuity, interest_rate, periods, inflation_rate=default_inflation_rate):
    real_interest_rate = get_real_interest_rate(inflation_rate, interest_rate)
    numerator = pow(1 + real_interest_rate, periods) - 1
    return numerator * annuity / real_interest_rate


def present_to_annuity(present, interest_rate, periods, inflation_rate=default_inflation_rate):
    real_interest_rate = get_real_interest_rate(inflation_rate, interest_rate)
    numerator = real_interest_rate * pow(1 + real_interest_rate, periods)
    denominator = pow(real_interest_rate + 1, periods) - 1
    return present * numerator / denominator


def annuity_to_present(annuity, interest_rate, periods, inflation_rate=default_inflation_rate):
    real_interest_rate = get_real_interest_rate(inflation_rate, interest_rate)
    numerator = pow(1 + real_interest_rate, periods) - 1
    denominator = real_interest_rate * pow(real_interest_rate + 1, periods)
    return numerator * annuity / denominator
