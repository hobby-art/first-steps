# Table data to be used for formating.
tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def printTable(table):

    # Define how much we need to justify for each column.
    colWidths = [0] * len(table)
    # Simply compare the length of the next item of a list with the previous item. Loop for each column (sublist).
    for i, sub_list in enumerate(table):
        for item in sub_list:
            if len(item) > colWidths[i]:
                colWidths[i] = len(item)


    # Define how many rows we need.
    num_rows = len(table[0])
    # Print the first item of each sublist in one row, then the second, and so forth.
    for row_index in range(num_rows):
        for i, sub_list in enumerate(table):
            print(sub_list[row_index].rjust(colWidths[i]), end=" ")
        print()


printTable(tableData)
