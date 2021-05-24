# Testing 'and', 'not', and 'or' statements

# has_high_income = False
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for a loan.")
else:
    print("Cannot apply for loan")