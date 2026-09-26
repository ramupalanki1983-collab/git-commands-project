def print_heading(title):
    print("Learning platform")
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)


def calculate_course_fee(fee, discount_percentage):
    discount = fee * discount_percentage / 100
    return fee - discount