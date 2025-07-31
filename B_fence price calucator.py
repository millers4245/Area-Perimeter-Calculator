def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine

keep_going = ""
while keep_going == "":
    # Get width and height
    width =  num_check("Width: ")
    height = num_check("Height: ")
    cost = num_check("Cost / m: ")


    # Calculate perimeter and price for the fence

    perimeter = 2 * (width + height)
    price = cost * perimeter

    # Display output
    print ()
    print(f"Perimeter: {perimeter}m units")
    print(f"Price: ${price: .2f}")

    # ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the fence price calculator")
