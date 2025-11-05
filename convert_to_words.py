def convert_to_words(liczba):
    """
    Convert a number to Polish words (for invoice amounts).
    Example: 1845.60 -> "tysiąc osiemset czterdzieści pięć złotych 60 groszy"
    """
    # Handle empty or invalid input
    if not liczba:
        return ""
    
    # Convert to string if it's a number
    if isinstance(liczba, (int, float)):
        liczba_str = f"{liczba:.2f}"
    else:
        liczba_str = str(liczba)
    
    # Handle Polish format (comma) or English format (period)
    # Replace comma with period for consistent processing
    liczba_str = liczba_str.replace(',', '.')
    
    # Split into integer and decimal parts
    parts = liczba_str.split('.')
    integer_part = int(parts[0])
    decimal_part = int(parts[1]) if len(parts) > 1 and parts[1] else 0
    
    # Convert integer part to words
    integer_words = number_to_polish_words(integer_part)
    
    # Add currency
    if integer_part == 1:
        integer_words += " złoty"
    elif integer_part % 10 in [2, 3, 4] and integer_part % 100 not in [12, 13, 14]:
        integer_words += " złote"
    else:
        integer_words += " złotych"
    
    # Add grosze if needed
    if decimal_part > 0:
        decimal_words = number_to_polish_words(decimal_part)
        integer_words += f" {decimal_words}"
        if decimal_part == 1:
            integer_words += " grosz"
        elif decimal_part % 10 in [2, 3, 4] and decimal_part % 100 not in [12, 13, 14]:
            integer_words += " grosze"
        else:
            integer_words += " groszy"
    
    return integer_words


def number_to_polish_words(n):
    """Convert integer to Polish words."""
    if n == 0:
        return "zero"
    
    if n < 0:
        return "minus " + number_to_polish_words(-n)
    
    # Single digits
    single_digits = ["", "jeden", "dwa", "trzy", "cztery", "pięć", 
                     "sześć", "siedem", "osiem", "dziewięć"]
    
    # 10-19
    teens = ["dziesięć", "jedenaście", "dwanaście", "trzynaście", 
             "czternaście", "piętnaście", "szesnaście", "siedemnaście", 
             "osiemnaście", "dziewiętnaście"]
    
    # Tens
    tens = ["", "", "dwadzieścia", "trzydzieści", "czterdzieści", 
            "pięćdziesiąt", "sześćdziesiąt", "siedemdziesiąt", 
            "osiemdziesiąt", "dziewięćdziesiąt"]
    
    # Hundreds
    hundreds = ["", "sto", "dwieście", "trzysta", "czterysta", 
                "pięćset", "sześćset", "siedemset", "osiemset", "dziewięćset"]
    
    # Thousands
    thousands = ["", "tysiąc", "dwa tysiące", "trzy tysiące", "cztery tysiące"]
    
    result = []
    
    # Thousands
    if n >= 1000:
        thousands_part = n // 1000
        if thousands_part == 1:
            result.append("tysiąc")
        elif thousands_part in [2, 3, 4]:
            result.append(thousands[thousands_part])
        else:
            result.append(number_to_polish_words(thousands_part) + " tysięcy")
        n %= 1000
    
    # Hundreds
    if n >= 100:
        hundreds_digit = n // 100
        result.append(hundreds[hundreds_digit])
        n %= 100
    
    # Tens and ones
    if n >= 20:
        tens_digit = n // 10
        ones_digit = n % 10
        result.append(tens[tens_digit])
        if ones_digit > 0:
            result.append(single_digits[ones_digit])
    elif n >= 10:
        result.append(teens[n - 10])
    elif n > 0:
        result.append(single_digits[n])
    
    return " ".join(result)


''' Test the function
if __name__ == "__main__":
    test_numbers = [12.3,  1002, 104, 75, 6, 1]
    for num in test_numbers:
        print(f"{num}: {convert_to_words(num)}")
'''