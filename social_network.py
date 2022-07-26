import social_network_classes


def goBack():
    use_account()


def use_account():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    choice = input("Please Choose a number: ")
    if choice == "1":
        first_name = input("What is your first name: ")
        last_name = input("What is your last name: ")
        firstname_file = open("firstname.txt", "w")
        firstname_file.writelines(first_name)
        firstname_file.close()
        lastname_file = open("lastname.txt", "w")
        lastname_file.writelines(last_name)
        lastname_file.close()
        new_age = input("What i(s your current age: ")
        age_file = open("age.txt", "w")
        age_file.writelines(new_age)
        age_file.close()
        account = social_network_classes.CreateAccount(first_name, last_name)
        account.account_create()
        goBack()
    elif choice == "2":
        print("1. Edit my details")
        print("2. Add a friend")
        print("3. View all my friends")
        print("4. View all my messages")
        print("5. Block a friend")
        print("6. <- Go back ")
        choice = input("Please Choose a number: ")
        if choice == "1":
            f = open("firstname.txt", "r")
            name_contents = f.read()
            f.close
            f = open("lastname.txt", "r")
            lastname_contents = f.read()
            f.close
            print("Your current name is: ", name_contents, lastname_contents)
            f = open("age.txt", "r")
            file_contents = f.read()
            print("Your current age is: ", file_contents)
            f.close
        elif choice == "2":
            friend_name = input("Enter the name of the friend: ")
            print("friend request to", friend_name, "has been sent")
            friend_requests_file = open("friendrequests.txt", "a")
            friend_requests_file.writelines(friend_name)
            friend_requests_file.writelines("\n")
            friend_requests_file.close()
        elif choice == "3":
            print("These are your current sent friend requests: ")
            f = open("friendrequests.txt", "r")
            friend_contents = f.read()
            f.close
            print(friend_contents)
        elif choice == "4":
            f = open("friendrequests.txt", "r")
            friend_contents = f.read()
            f.close
            print("You can currently send messages to:\n")
            with open("friendrequests.txt", "r") as f:
                number = 1
                for line in f:
                    print(number, ".", line)
                    number += 1
            message_to = input("Who would you like to send a message to: ")
            person = message_to + "message.txt"
            message = input("Type your message here: ")
            messages_file = open(person, "a")
            messages_file.writelines(message)
            messages_file.writelines("\n")
            messages_file.close()
            f = open(person, "r")
            message_contents = f.read()
            f.close
            print(message_contents)
        elif choice == "5":
            print("These are your current friends: ")
            with open("friendrequests.txt", "r") as f:
                number = 1
                for line in f:
                    print(number, ".", line)
                    number += 1
            block_name = input(
                "Who would you like to block?\nEnter a number: ")
            with open('friendrequests.txt', 'r') as fr:
                # reading line by line
                lines = fr.readlines()

                # pointer for position
                ptr = 1
                with open('friendrequests.txt', 'w') as fw:
                    for line in lines:

                        # we want to remove 5th line
                        if ptr != block_name:
                            fw.write(line)
                        ptr += 1

            print("Deleted")

        elif choice == "6":
            goBack()


use_account()
