import sys
import shelve

# Function to print usage instructions
def print_usage():
    print('Usage:')
    print('  python multiclipboard.py <command> <keyword> [<value>]')
    print('Commands:')
    print('  save <keyword> <value>  - Saves a clipboard value with a keyword')
    print('  delete <keyword>  - Deletes a specific keword')
    print('  list  - List all saved keywords')

# Main program logic
def main():
    # Check if the user has provided arguments
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()

    # Open the shelve database
    with shelve.open('multiclipboard.dat') as shelf:
        if command == 'save' and len(sys.argv) == 4:
            keyword = sys.argv[2]
            value = sys.argv[3]
            shelf[keyword] = value
            print(f'Saved value under keyword: {keyword}')
        elif command == 'delete' and len(sys.argv) == 3:
            keyword = sys.argv[2]
            if keyword in shelf:
                del shelf[keyword]
                print(f'Deleted keyword: {keyword}')
            else:
                print(f'Keyword "{keyword}" not found')
        elif command == 'delete' and len(sys.argv) == 2:
            shelf.clear()  # Delete all keywords
            print('Deleted all keywords.')
        elif command == 'list':
            if shelf:
                print('Saved keywords:')
                for keyword in shelf:
                    print(f'   {keyword}')
            else:
                print('No keywords saved.')
        else:
            print_usage()

if __name__ == '__main__':
    main()
