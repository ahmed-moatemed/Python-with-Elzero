# --------------------------------------------------------
# -- Advanced Lessons => Generate Random Serial Numbers --
# --------------------------------------------------------

import string
import random

# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

def make_serial(size):

    all_chars = string.ascii_letters + string.digits
    # print(all_chars)

    chars_count =len(all_chars)
    # print(chars_count)

    serial_list = []

    while size > 0:

        random_num = random.randint(0, chars_count - 1)

        random_character = all_chars[random_num]

        serial_list.append(random_character)

        size -= 1

    print("".join(serial_list))


make_serial(20)
make_serial(30)
make_serial(10)

