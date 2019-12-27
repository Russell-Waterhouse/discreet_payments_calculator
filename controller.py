import sys
import calculate_value


def main():
    operation = get_type_of_calculation()
    if operation == 0:
        exit(0)
    elif operation == 1:
        present_of_future()
    elif operation == 2:
        #     TODO: finish this operation
        print("feature under development")
    elif operation == 3:
        future_of_present()
    elif operation == 4:
        #         TODO: finish this operation
        print("feature under development")


def future_of_present():
    present_value = get_present_value()
    go_back_if_none(present_value)
    interest_rate = get_interest_rate()
    go_back_if_none(interest_rate)
    periods = get_num_periods()
    go_back_if_none(periods)
    future_value = calculate_value.present_to_future(present_value, interest_rate, periods)
    print("the future value of ", present_value, " is ", future_value)
    main()


def present_of_future():
    future_value = get_future_value()
    go_back_if_none(future_value)
    interest_rate = get_interest_rate()
    go_back_if_none(interest_rate)
    periods = get_num_periods()
    go_back_if_none(periods)
    present_value = calculate_value.future_to_present(future_value, interest_rate, periods)
    print("The present value of ", future_value, " is ", present_value)
    main()


def go_back_if_none(test_value):
    if test_value is None:
        main()
        exit(0)


def get_num_periods():
    print("Please enter the number of periods between the present time and the future time in question")
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
    print("press 2 to calculate the present value of a future amount with inflation")
    print("press 3 to calculate the the future value of a present amount")
    print("press 4 to calculate the the future value of a present amount with inflation")
    print("press 5 to calculate the present value of an annuity")
    print("press 6 to calculate the present value of an annuity with inflation")

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
