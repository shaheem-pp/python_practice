product = ["tomato", "carrot", "milk", "bread", "snack"]
price = [20, 15, 24, 35, 10]
purchased = []
exit = 1


def find_duplicates(array):
    count = {}
    for item in array:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    duplicates = {k: v for k, v in count.items() if v > 1}
    return count


def generate_invoice(purchased):
    purchased.sort()
    purchases = find_duplicates(purchased)
    print(purchases)



while exit == 1:
    print("What you want to buy?")
    for i in range(5):
        print(i + 1, "-", product[i], "-", price[i])
    print(6, "- to exit")
    user_input = int(input("Enter the number"))
    if user_input >= 1 and user_input <= 5:
        purchased.append(user_input - 1)
    else:
        generate_invoice(purchased)
        exit = 0

# product = ["tomato", "carrot", "milk", "bread", "snack"]
# price = [20, 15, 24, 35, 10]
# purchased = []
# exit = 1
#
#
# def generate_invoice(purchased):
#     total_price = 0
#     print("Invoice:")
#     for item in purchased:
#         print("-", product[item], price[item])
#         total_price += price[item]
#     print("Total Price:", total_price)
#     return
#
#
# while exit == 1:
#     print("What you want to buy?")
#     for i in range(5):
#         print(i + 1, "-", product[i], "-", price[i])
#     print(6, "- to exit")
#     user_input = int(input("Enter the number"))
#     if user_input >= 1 and user_input <= 5:
#         purchased.append(user_input - 1)
#     else:
#         generate_invoice(purchased)
#         exit = 0
