def calculate_price(fish_type, hours):
    market_price = 50000

    if hours < 0:
        return "Input không hợp lệ"

    if fish_type == "Cá Trắm Đen" or fish_type == "Cá Thu":
        if 0 <= hours <= 8:
            return market_price * 1.2
        elif 9 <= hours <= 16:
            return market_price * 0.8
        else:
            return "Mang về cho heo ăn"
    else:
        return "Unknown fish type"


def main():
    print("Welcome to Cá Xanh Market")

    fish_type = input("Enter fish type (Cá Trắm Đen or Cá Thu): ")
    hours = int(input("Enter the number of hours since the fish was caught (0-16): "))

    result = calculate_price(fish_type, hours)
    print(f"The price for {fish_type} after {hours} hours is: {result}")


if __name__ == '__main__':
    main()
