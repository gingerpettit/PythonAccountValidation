# This program asks the user to input an account number and tells the user
# whether the account number is in the list or not.

def main():
    infile=open("charge_accounts.txt") #Open file for reading.
    useraccounts=infile.readlines() #Read the contents of file into a list.
    infile.close() #Close the file
    index=0
    while index < len(useraccounts):    # Convert file into Int.
        useraccounts[index]=int(useraccounts[index])
        index+=1

    userInputAccount=int(input("Enter the account number: "))  #Get user input for the account number.

    if userInputAccount in useraccounts:  #Determine if the user input is in the file.
        print("The account number ", userInputAccount," is valid.")
    else:
        print("The account number ", userInputAccount," is not valid.")


main()