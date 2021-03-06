import sys

import calculate_value

'''
    print("press 0 to exit the program")
    print("press 1 to calculate the present value of a future amount")
    print("press 2 to calculate the future value of a present amount")
    print("press 3 to calculate the future value of an annuity")
    print("press 4 to calculate an annuity from a future amount")
    print("press 5 to calculate the present value of an annuity")
    print("press 6 to calculate an annuity from a present amount")
    '''


def main():
    operation = get_type_of_calculation()
    if operation == 0:
        exit(0)
    elif operation == 1:
        present_of_future()
    elif operation == 2:
        future_of_present()
    elif operation == 3:
        future_of_annuity()
    elif operation == 4:
        annuity_of_future()
    elif operation == 5:
        present_of_annuity()
    elif operation == 6:
        annuity_of_present()
    else:
        print("This value is not recognized. Please try again \n")
        main()


def annuity_of_present():
    present_value = get_present_value()
    go_back_if_none(present_value)
    interest = get_interest_rate()
    go_back_if_none(interest)
    periods = get_num_periods()
    go_back_if_none(periods)
    inflation = get_inflation()
    go_back_if_none(inflation)
    annuity = calculate_value.present_to_annuity(present_value, interest, periods, inflation)
    print("the annuity of the present amount ", present_value, " is ", annuity)
    main()


def annuity_of_future():
    future_value = get_future_value()
    go_back_if_none(future_value)
    interest_rate = get_interest_rate()
    go_back_if_none(interest_rate)
    periods = get_num_periods()
    go_back_if_none(periods)
    inflation = get_inflation()
    go_back_if_none(inflation)
    annuity = calculate_value.future_to_annuity(future_value, interest_rate, periods, inflation)
    print("The annuity of the future amount ", future_value, " is ", annuity)
    main()


def future_of_annuity():
    annuity = get_annuity_value()
    go_back_if_none(annuity)
    periods = get_num_periods()
    go_back_if_none(periods)
    interest_rate = get_interest_rate()
    go_back_if_none(interest_rate)
    inflation_rate = get_inflation()
    future_value = calculate_value.annuity_to_future(annuity, interest_rate, periods, inflation_rate)
    print("the future value of ", annuity, " annuity for ", periods, " periods is ", future_value)
    main()


def present_of_annuity():
    annuity = get_annuity_value()
    go_back_if_none(annuity)
    periods = get_num_periods()
    go_back_if_none(periods)
    interest_rate = get_interest_rate()
    go_back_if_none(interest_rate)
    inflation_rate = get_inflation()
    go_back_if_none(inflation_rate)
    present_value = calculate_value.annuity_to_present(annuity, interest_rate, periods, inflation_rate)
    print("the present value of ", annuity, " annuity for ", periods, " periods is ", present_value)
    main()


def future_of_present():
    present_value = get_present_value()
    go_back_if_none(present_value)
    interest_rate = get_interest_rate()
    go_back_if_none(interest_rate)
    periods = get_num_periods()
    go_back_if_none(periods)
    inflation = get_inflation()
    go_back_if_none(inflation)
    future_value = calculate_value.present_to_future(present_value, interest_rate, periods, inflation)
    print("the future value of ", present_value, " is ", future_value)
    main()


def present_of_future():
    future_value = get_future_value()
    go_back_if_none(future_value)
    interest_rate = get_interest_rate()
    go_back_if_none(interest_rate)
    periods = get_num_periods()
    go_back_if_none(periods)
    inflation = get_inflation()
    go_back_if_none(inflation)
    present_value = calculate_value.future_to_present(future_value, interest_rate, periods, inflation)
    print("The present value of ", future_value, " is ", present_value)
    main()


def go_back_if_none(test_value):
    if test_value is None:
        main()
        exit(0)


def get_annuity_value():
    print("please enter the annuity value for this period or 'b' to go back")
    return get_int_input()


def get_inflation():
    print("please enter the inflation that you expect over this period or 'b' to go back")
    return get_float_input()


def get_num_periods():
    print("Please enter the number of periods between the present time and the future time in question\n"
          "alternatively, enter 'b' to go back")
    return get_int_input()


def get_future_value():
    print("Please enter the future value below or 'b' to go back")
    return get_float_input()


def get_present_value():
    print("Please enter the present value below or 'b' to go back")
    return get_float_input()


def get_interest_rate():
    print("please enter the interest rate below or 'b' to go back")
    return get_float_input()


def get_int_input():
    user_input = sys.stdin.readline()
    if user_input == 'b':
        return None
    try:
        user_input = int(user_input)
        return user_input
    except ValueError:
        print("That value was not expected. please enter a number with no decimals in it")
        return get_float_input()


def get_float_input():
    user_input = sys.stdin.readline()
    if user_input == 'b':
        return None
    try:
        user_input = float(user_input)
        return user_input
    except ValueError:
        print("That value was not expected. please enter a number")
        return get_float_input()


def get_type_of_calculation():
    print("press 0 to exit the program")
    print("press 1 to calculate the present value of a future amount")
    print("press 2 to calculate the future value of a present amount")
    print("press 3 to calculate the future value of an annuity")
    print("press 4 to calculate an annuity from a future amount")
    print("press 5 to calculate the present value of an annuity")
    print("press 6 to calculate an annuity from a present amount")

    user_input = sys.stdin.readline()
    try:
        user_input = int(user_input)
    except ValueError:
        user_input = -1
    if 0 <= user_input < 7:
        return user_input
    else:
        print("That was not an expected value. please enter a number 0-6 that corresponds to the desired operation")
        return get_type_of_calculation()


if __name__ == '__main__':
    main()
