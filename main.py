print("\t\tSMARTPHONE DIRECTORY", flush=False)

print("\tYou can now perform the following operation on this\nslambook\n")
print("1. Add a new contact")
print("6. Exit phonebook")

def add_contact(pb):
    # Adding a contact is the easiest because all you need to do
    # is: append another list of details into the already existing list
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(int(input("Enter number: ")))
        if i == 2:
            dip.append(str(input("Enter e-mail address: ")))
        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
        if i == 4:
            dip.append(str(input("Enter category (Family/Friends/work/Others): ")))
    pb.append(dip)
    # And once you modify the list, you return it to the calling function, here
    return pb
def thanks():
    # A simple gesture of courtesy towards the user to enhance user experience
    print("******************************************************")
    print("Thank you for using our Slam Book.")
    print("Please visit again!")
    print("******************************************************")
    sys.exit("Goodbye, have a nice day ahead!")

# Main function code
print("........................................................")
print("Hello dear Friends, welcome to our Slam Book")
print("You may now proceed to explore this Slam Book and fill your details about your friends")
# This is solely meant for decoration purpose only.
# You're free to modify your interface as per your will to make it look interactive
ch = 1
pb = initial_slambook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 4:
        pb = add_contact(pb)
    else:
        thanks()
