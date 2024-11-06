PLACEHOLDER = "[name]"

with open("names.txt", "r") as names:
    names_list = names.readlines()

with open("Invitation.txt") as invite:
    invitation_contents = invite.read()
    for name in names_list:
        stripped_names = name.strip()
        new_invitation = invitation_contents.replace(f"{PLACEHOLDER}", f"{name}")
        with open(f"C:\\Users\HP\Desktop\pythonProject\Files_lessons\Ready To Send\\letter for {stripped_names}.txt", "w") as ready:
            ready.write(new_invitation)

