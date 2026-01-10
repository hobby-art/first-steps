tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def printTable(table):

    colWidths = [0] * len(table)

    for i, sub_list in enumerate(table):
        for item in sub_list:
            if len(item) > colWidths[i]:
                colWidths[i] = len(item)

    num_rows = len(table[0])

    for row_index in range(num_rows):
        for i, sub_list in enumerate(table):
            print(sub_list[row_index].rjust(colWidths[i]), end=" ")
        print()


printTable(tableData)
