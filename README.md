# discreet_payments_calculator

This is a discreet payment calculator CLI script written in python.  

It is a quick implementation of the formula sheet provided to students in ECON180.  
It is useful for turning annuities into net present values, and other fun
things that you learn in a first year project economics course. 

# To run the calculator:
Run the following command:
```
python3 main.py
```

After this, follow the prompts for a full interactive experience.

## Example usage:
```
$ python3 main.py

press 0 to exit the program
press 1 to calculate the present value of a future amount
press 2 to calculate the future value of a present amount
press 3 to calculate the future value of an annuity
press 4 to calculate an annuity from a future amount
press 5 to calculate the present value of an annuity
press 6 to calculate an annuity from a present amount

$ 5

please enter the annuity value for this period or 'b' to go back

$ 15000

Please enter the number of periods between the present time and the future time in question
alternatively, enter 'b' to go back

$ 4

please enter the interest rate below or 'b' to go back

$ 0.08

please enter the inflation that you expect over this period or 'b' to go back

$ 0.03

the present value of  15000  annuity for  4  periods is  53369.68434495787
```

# To Run the Tests:
```
python -m unittest test_calculate_value.py
```
