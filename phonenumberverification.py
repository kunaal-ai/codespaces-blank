def is_valid_phone_number(phone_number: str):
    res = False

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

    if "-" in phone_number and len(phone_number) == 12:
        if phone_number[3] == "-" and phone_number[7] == "-":  # verifies if - on intended place
            phone_number = phone_number.replace("-", "")
            res = is_digit(phone_number)  # verify if all are digit and set that True / False

    elif "-" not in phone_number and len(phone_number) == 10:
        res = is_digit(phone_number)  # verify if all are digit and set that True / False

    return res


# Test cases
print(is_valid_phone_number("123-456-7890"))  # True
print(is_valid_phone_number("2224445555"))  # True
print(is_valid_phone_number("222-444-555"))  # False
print(is_valid_phone_number("22a-44b-555c"))  # False
print(is_valid_phone_number("  abc-def-ghij "))  # False
#print(is_valid_phone_number("  "))  # Value Error
#print(is_valid_phone_number(222 - 444 - 555))  # Type Error
