def phone_number_validation(phone_number: str):
    """ Phone number as a string input and validate if as per business rules.
            - acceptable formats are 000-000-0000 or 1112223456
            - should not accept alphabets , only digits allowed
            - length=12 with - or length = 10 without -
        Args:
            phone_number: str - user input phone number as a string
    """
    resopnse = False

    # check-point
    # TypeError
    if not isinstance(phone_number, str):
        raise TypeError("error: input not a string")
    # value error
    if len(phone_number) < 10:
        raise ValueError("error: expecting 10 or 15 characters")

    # sanitization
    phone_number = phone_number.strip()

    def is_digit(p_number: str):
        """ Verifies if the given p_number is a digit or not
        Args:
            p_number (str)
        """
        verified = False
        for i in p_number:
            if i.isdigit():
                verified = True
            else:
                verified = False
                break
        return verified

    # case 01- if "-" in phone number
    if "-" in phone_number and len(phone_number) == 12:
        if phone_number[3] == "-" and phone_number[7] == "-":  # verifies if - on intended place
            phone_number = phone_number.replace("-", "")
            resopnse = is_digit(phone_number)  # verify if all are digit and set that True / False

    # case 02- if NO "-" in phone number
    elif "-" not in phone_number and len(phone_number) == 10:
        resopnse = is_digit(phone_number)  # verify if all are digit and set that True / False

    return resopnse


# Test cases
print(phone_number_validation("123-456-7890"))  # True
print(phone_number_validation("2224445555"))  # True
print(phone_number_validation("222-444-555"))  # False
print(phone_number_validation("22a-44b-555c"))  # False
print(phone_number_validation("  abc-def-ghij "))  # False
#print(phone_number_validation("  "))  # Value Error
#print(phone_number_validation(222 - 444 - 555))  # Type Error
