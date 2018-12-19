"""" A demo on List and string"""
# Creating Function to Process file

def get_user_list(data_file, target_file):
    """"
    :get's the list of user
    :param data_file: str
    :param target_file: str
    :return:
    """
    list_of_users = []  # Empty list defining

    try:
        for line in open(data_file):
            login = line.split(':')[0]
            list_of_users.append(login) # Appending the login user to the Empty List
        list_of_users.sort()  # Sorthing it in Alphabetic order

        with open(target_file, 'w') as result: # Context manager to wite output in the Target File
            for line_no, user in enumerate(list_of_users, 1): # Index of the element is start with 0, we have to mention '1' as the corresponding
                formatted_content = "{:>6} {}".format(line_no, user)
                print(formatted_content)
                result.write(formatted_content + "\n")

    except (FileNotFoundError, IOError) as err:
        print(err)

file_name = input('Enter the File Name :')
get_user_list(file_name, 'password.dat')
