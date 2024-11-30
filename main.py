def calculate_split(total_amount: float, shares: list, currency: str) -> None:
    print(f'Total expense: {currency} {total_amount:,.2f}')
    print(f'Number of people: {len(shares)}')
    for i, share in enumerate(shares, 1):
        print(f'Person {i} should pay: {currency} {share:,.2f}')

def main() -> None:
    while True:
        try:
            total_amount: float = float(input("Enter the total amount of the expense: "))
            number_of_people: int = int(input("Enter the number of people sharing the expense: "))
            if number_of_people < 1:
                raise ValueError("Number of people must be greater than zero")

            uneven_split: str = input("Do you want uneven splits? (yes/no): ").strip().lower()
            shares = []

            if uneven_split == 'yes':
                print("Enter each person's share as a percentage of the total amount")
                total_percentage = 0

                for i in range(number_of_people):
                    percentage = float(input(f"Enter a percentage for person {i + 1}: "))
                    if percentage <= 0 or percentage > 100:
                        raise ValueError("Percentage must be between 1 and 100")
                    total_percentage += percentage
                    shares.append(total_amount * (percentage/100))

                if abs(total_percentage - 100) > 0.01:
                    raise ValueError("Total percentage must equal 100%")
            else:
                shares_per_person = total_amount / number_of_people
                shares = [shares_per_person] * number_of_people

            calculate_split(total_amount, shares, currency="INR")
            break

        except ValueError as e:
            print(f"Error: {e}. Please Try again.")

if __name__ == '__main__':
    main()
