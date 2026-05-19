def has_digit_in_password(password):
    return any(symbol.isdigit() for symbol in password)

def get_password(password):
    return any(not symbol.isdigit() and symbol.isalpha() for symbol in password)

def get_lenght(password):
    return len(password) > 12
    
def has_leters_in_password(password):
    return any(symbol.isalpha() for symbol in password)
        
def has_high_leters_in_password(password):
    return any(symbol.isupper() for symbol in password)
    
def main():

    password = input("Введите пароль:")
    score = 0

    functions = [
        has_leters_in_password(password),
        get_password(password),
        has_high_leters_in_password(password),
        has_digit_in_password(password),
        get_lenght(password)
    ]

    for function in functions:
        if function:
            score += 2

    print(f"Рейтинг пароля:{score}")

if __name__ == "__main__":
    main()
