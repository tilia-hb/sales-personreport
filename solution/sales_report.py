"""Generate sales report showing total melons each sales person sold."""


# ORIGINAL LIST ANSWER


def print_sales_report(sales_report):
    """Printable version of sales report. Count total melons per salesperson."""

    # Instantiate lists to hold information by index.
    salespeople = []
    melons_sold = []

    # Open the file, split each line on the pipe ("|"), and iterate over each
    # new list to save salesperson and melon to variables for the duration of
    # the single line iteration.

    report = open(sales_report)
    for line in report:
        line = line.rstrip()
        entries = line.split("|")
        salesperson = entries[0]
        melons = int(entries[2])

        # Check to see if salesperson already has a tally of sales.
        # If so, add. Else, add salesperson and tally to list.

        if salesperson in salespeople:
            position = salespeople.index(salesperson)
            melons_sold[position] += melons
        else:
            salespeople.append(salesperson)
            melons_sold.append(melons)

    # Print results organized by salesperson.
    for i in range(len(salespeople)):
        print("{} sold {:,} melons".format(salespeople[i], melons_sold[i]))


# ALTERNATE DICTIONARY ANSWER

def print_sales_report_dict(sales_report):
    sales_report_dict = {}

    report = open(sales_report)
    for line in report:
        line = line.rstrip()
        entries = line.split("|")
        salesperson = entries[0]
        melons = int(entries[2])
        if salesperson in sales_report_dict:
            sales_report_dict[salesperson] += melons
        else:
            sales_report_dict[salesperson] = melons

    for salesperson, melon_count in sales_report_dict.items():
        print("{} sold {:,} melons".format(salesperson, melon_count))


print_sales_report("sales-report.txt")
