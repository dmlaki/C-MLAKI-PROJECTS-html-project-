def main():
    # Prompt the user for their name
    name = input("What is your name? ")
    
    # Prompt the user for their age
    age = input("How old are you? ")
    
    # Prompt the user for their location
    location = input("Where are you located? ")
    
    # Print a personalized message
    print("\nHello, {}! It's nice to meet you.".format(name))
    print("You are {} years old, and you're located in {}.".format(age, location))
    print("Have a great day!")

if __name__ == "__main__":
    main()   


    