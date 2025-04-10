# SE T18 - Compulsory Task 1
# Student: Marius M
# Date: 15.06.2023

### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    # Declare the class variable, with default value, for emails. 
    has_been_read = False
    is_spam = False
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
    # Create the method to change 'is_spam' emails from False to True.
    def email_is_spam(self):
        self.is_spam = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.

# function populate_inbox() with no parameters
# creates 3 new Email objects and adds them to the inbox list
def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list.
    inbox.append(Email("sarah.smith@aol.com", "New project enquiry", "Hello Dan,\nI hope that you are well!\n\nCan you please send the budget code for the new project?\nThanks!"))
    inbox.append(Email("john.godwell@aol.com", "Please send the report", "Hi Dan,\nI need that report asap!!!\n\nPlease send it by the end of today!\nRegards, John!"))
    inbox.append(Email("sarah.smith@aol.com", "Friday event", "Hey Dan,\nI hope that everything is going well!\n\nPlease let us know if you are joining at the Black Sheep pub event this Friday!\nThanks, Sarah"))

# function list_emails() with no parameters
# prints all the emails from inbox list and allows the user to read, mark as spam or delete a certain email
def list_emails(): 
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    # Print a message if there are no emails int the inbox
    if (len(inbox) == 0):
        print("Notice: There are no emails in the inbox!")
    else:
        # print all the emails from inbox list
        for index, email in enumerate(inbox):
            spam = "\t Spam!" if email.is_spam == True else ""
            print(f"{index}.\t{email.subject_line}{spam}")
        # ask the user to input the email that wants to address
        while True:
            try:
                emailNo = int(input("Please enter the email number that you want to address: "))
                # if the email number is not found or less than 0 print an error message
                if (emailNo > len(inbox)-1 or emailNo < 0):
                    print("Error: The email that you have selected doesn't exists!")
                else:
                    # ask the user to input the option for the selected email
                    while True:
                        print("Please select one of the following options:\n1 - Read the email\n2 - Mark as spam\n3 - Delete the email\n4 - Exit")
                        option = int(input())
                        # if option 1 was selected call read_email()
                        if option == 1:
                            read_email(emailNo)
                            break
                        # if option 2 was selected mark the email as spam and print a message
                        elif option == 2:
                            inbox[emailNo].email_is_spam()
                            print(f"Notice: The email \"{emailNo}. {inbox[emailNo].subject_line}\" has been marked as spam!")
                            break
                        # if option 3 was selected delete the email and print a message
                        elif option == 3:
                            emailDeleted = inbox.pop(emailNo)
                            print(f"Notice: The email \"{emailNo}. {emailDeleted.subject_line}\" has been deleted!")
                            break
                        # if option 4 was selected exit the while
                        elif option == 4:
                            break
                        # else print an error message
                        else:
                            print("Error: The option that you selected doesn't exist!")
                    break
            except ValueError:
                print("Error: Please enter a number!")

# function read_email() with one int parameter index
# prints out all the details of a certain email and marks the email as read
def read_email(index):
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    print(f"{index}.\t{inbox[index].subject_line}")
    print(f"Sent by: {inbox[index].email_address}")
    print(inbox[index].email_content)
    inbox[index].mark_as_read()
    print(f"\nNotice: Email from {inbox[index].email_address} marked as read.")

# --- Email Program --- #
# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.
print("Welcome to your email client!")
while True:
    while True:
        # use input to get the option that the user requires
        try:
            user_choice = int(input('''\nMenu
        Would you like to:
        1. Read an email
        2. View unread emails
        3. Quit application

Enter selection: '''))
            # if the user selects option 1 call the list_emails() function
            if user_choice == 1:
                # add logic here to read an email
                print("Option 1 - Read an email: ")
                list_emails()
            # if the user selects option 2 print out all the unread emails
            elif user_choice == 2:
                # add logic here to view unread emails
                print("Option 2 - View unread emails: ")
                unread = False
                for index, email in enumerate(inbox):
                    if (email.has_been_read == False):
                        spam = "\t Spam!" if email.is_spam == True else ""
                        print(f"{index}.\t{email.subject_line}{spam}")
                        unread = True
                # print a notice message if there are no unread messages
                if unread == False:
                    print("Notice: There are no unread messages in the inbox!")
            # if the user selects option 3 exit the program
            elif user_choice == 3:
                # add logic here to quit appplication
                print("Notice: Thank you for using the email client! Goodbye!")
                exit()
            # else return an error message
            else:
                print("Error: The option that you have selected doesn't exist!")
        except ValueError:
            print("Error: Please enter a number!")
