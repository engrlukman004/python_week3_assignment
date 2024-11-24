def calculate_discount(price, discount):
    if discount > 20:
        discounted_price = price - (price*discount*0.01)
        print(discounted_price)
    else:
        print(price);
calculate_discount(int(input('input the price and the discount in percentage: ')))
