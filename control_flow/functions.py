def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

def main():
    # Prompting the user for input
    original_price = float(input("Enter the original price of the item: $"))
    discount_input = input("Enter the discount percentage: ")
    
    # Removing the percentage sign and converting to float
    discount_percent = float(discount_input.rstrip('%'))
    
    # Calculating the final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Printing the result
    if final_price == original_price:
        print("No discount applied. Final price: ${:.2f}".format(final_price))
    else:
        print("Final price after applying {}% discount: ${:.2f}".format(discount_percent, final_price))

if __name__ == "__main__":
    main()
