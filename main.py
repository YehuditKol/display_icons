import displayIcons


def main():
    try:
        x = input("Select an option:\n'1' to Print all icons.\n or search icons by keyword\n")
        if x == '1':
            displayIcons.print_all_icons()
        else:
            arr = displayIcons.search_icons_by_keyword(x)
        icon = input("Select one icon from the search list to display on the screen:\n")
        displayIcons.display_icon(icon,arr)
    except Exception as e:
        print("An error occurred:", e)


main()


