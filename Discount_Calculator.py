def calculator():

    price = float(input('Selling Price: '))

    discount_percentage = float(input('Discount % : '))

    total = price * discount_percentage / 100

    final_price = price - total

    print(f'''
        Discount Price: ${total}
        Total price after discount: ${final_price}
    ''')

    check_another = input('Calculater another price? "y" or "n": ').lower()

    if check_another == 'y':
        calculator()

    else:
        exit()


calculator()
