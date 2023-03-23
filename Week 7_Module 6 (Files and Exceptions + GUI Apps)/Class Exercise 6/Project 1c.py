# Project #1 (Writing and Reading files)
# This function will allow the user to write the input
def WriteInput():

    print('enter the name of your friends')
    writeMoreFriends = 'Y'

    while writeMoreFriends == 'Y' or writeMoreFriends == 'y':

        name1 = input('Friend #1 ')
        name2 = input('Friend #2 ')
        name3 = input('Friend #3 ')

        FriendFile = open('friends.txt','a') # the a letter means to append

        FriendFile.write(name1 + '\n')
        FriendFile.write(name2 + '\n')
        FriendFile.write(name3 + '\n')

        FriendFile.close()

        print('friends recorded')

        writeMoreFriends = input('do you want to write more friends? type Y or y: ')

WriteInput()
