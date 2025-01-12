table_data = [['apples', 'orange', 'cherries', 'banana'],
              ['Alice', 'Bob','Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table(lists):
    # col_widths = [max(len(item) for item in col) for col in lists]
    
    col_widths = []
    
    for col in lists:
        max_width = 0
        for item in col:
            max_width = max(max_width, len(item))
        col_widths.append(max_width)
        
    for row in zip(*lists):
        for i in range(len(row)):
            print(row[i].rjust(col_widths[i]), end=' ')
        print()

print_table(table_data)
