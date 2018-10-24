'''
Author: Kyle Harvey 18473155
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: This program will process a file called data.txt.
'''
from datetime import datetime
import sys


def read_data(filename):
    '''
    read_data(filename):
    This will read in data from filename (e.g "data.txt") and will
    build a list of all the values converted into their respective
    types.
    '''
    # for each section we'll print a header and to make that easier
    # I first want to calculate the size needed to pad out the header
    # and make the size something standard (I chose 80 just like the
    # style guides would suggest)
    header_text = "Reading data"
    header_text_size = len(header_text)
    print("*" * (40 - (int(header_text_size/2) + 1)),
          header_text,
          "*" * (40 - (int(header_text_size/2) + 1)))
    print()  # prints an empty line for formatting purposes
    records = []
    try:
        with open(filename, 'r') as records_file:  # opened in read mode
            for line in records_file:
                rec = [x.strip() for x in line.split(",")]
                # rec[0] rec[1] and rec[5] are already strings
                # so don't need to be converted into anything else
                rec[2] = float(rec[2])  # year_revenue
                rec[3] = float(rec[3])  # revenue_growth
                rec[4] = int(rec[4])  # number_of_employees
                rec[6] = datetime.strptime(rec[6],  # 80 char limit
                                           "%d-%m-%Y")  # company_found_date
                records.append(rec)
    except FileNotFoundError:
        print("File:", filename, "was not found. Please fix before running.")
        sys.exit(1)  # using 1 as return value for program when we error
    print("\nDone reading data.\n\n")  # the section has completed
    return records


def print_all_records(records):
    '''
    print_all_records(data):
    This will take in a list of rows and for each row will print the values
    into a formatted table.
    '''
    header_text = "Printing records"
    header_text_size = len(header_text)
    print("*" * (40 - (int(header_text_size/2) + 1)),
          header_text,
          "*" * (40 - (int(header_text_size/2) + 1)))
    print()
    # I save the header words so I can calculate against their size
    # and use them as parameters into a formatted string
    name = "Name"
    industry = "Industry"
    revenue = "Revenue"
    revenue_growth = "Revenue growth"
    employees = "Employees"
    headquarters = "Headquarters"
    founded = "Founded"

    # The following lines are broken into pieces to fit inside the 80 char
    # limit. They are also really expensive calculations because they read
    # the records multiple times in different passes but with the end goal
    # of the printed table being adaptive to the size of the content. For
    # each column in the data passed in we calculate the max of len over
    # that column and we then calculate the max of the column values against
    # the header length Thus we will have column widths bigger than their
    # contents and bigger than their headers
    column_name = max(max(len(x[0]) for x in records) + 1,
                      len(name) + 1)
    # for example:
    # max -- trying to find size larger than header else returns header = 18
    # | \
    # |  header size (len(name) = "name" = 4) + 1 = 5
    # |
    # max -- trying to find largest row in column (returns 18 for Royal... +1)
    # | \ ... - many rows  the largest returned is Royal Dutch Shell = 17
    # |  \
    # |   \
    # x[0] x[1] ...
    # =       =
    #  Walmart CNP Corp ...
    column_industry = max(max(len(x[1]) for x in records) + 1,
                          len(industry) + 1)
    column_revenue = max(max(len(str(x[2])) for x in records) + 1,
                         len(revenue) + 1)
    column_revenue_growth = max(max(len(str(x[3])) for x in records) + 1,
                                len(revenue_growth) + 1)
    column_employees = max(max(len(str(x[4])) for x in records) + 1,
                           len(employees) + 1)
    column_headquarters = max(max(len(x[5]) for x in records) + 1,
                              len(headquarters) + 1)
    column_founded = max(max(len("{d.day}-{d.month}-{d.year}"
                             .format(d=x[6])) for x in records) + 1,
                         len(founded) + 1)

    # then I build the format string by using fstrings in-between
    # "{:<" and "}" the fstrings will replace {variable} with the
    # value from the variable that exists in the python context
    # in the end I'll have a format string that specifies the sizes
    # of each column based on the largest piece of content either
    # by value or by header
    table_format = "{:<" + f"{column_name}" + "}" + \
                   "{:<" + f"{column_industry}" + "}" + \
                   "{:<" + f"{column_revenue}" + "}" + \
                   "{:>" + f"{column_revenue_growth}" + "}" + \
                   "{:>" + f"{column_employees}" + "}" + \
                   "{:>" + f"{column_headquarters}" + "}" + \
                   "{:>" + f"{column_founded}" + "}"

    print(table_format.format("Name",
                              "Industry",
                              "Revenue",
                              "Revenue growth",
                              "Employees",
                              "Headquarters",
                              "Founded"))

    # we calculate the total width so we can create an underline
    # that makes thinks just a little more like a proper table
    total_column_width = sum([column_name,
                             column_industry,
                             column_revenue,
                             column_revenue_growth,
                             column_employees,
                             column_headquarters,
                             column_founded])

    print("-" * total_column_width)

    # and finally we print the table with some mild formatting
    for rec in records:
        print(table_format.format(rec[0],
                                  rec[1],
                                  str(rec[2]),
                                  "{:.2f}".format(rec[3]),
                                  rec[4],
                                  rec[5],
                                  rec[6].strftime("%d/%m/%Y")))
    print()  # print a single empty line for formatting purposes


def print_positive_growth(records):
    '''
    print_positive_growth(records):
    We will print out all the companies that match the criteria of having a
    revenue growth that is positive.
    '''
    header_text = "Print companies with positive growth"
    header_text_size = len(header_text)
    print("*" * (40 - (int(header_text_size/2) + 1)),
          header_text,
          "*" * (40 - (int(header_text_size/2) + 1)))
    print()
    # we'll reuse part of the program to print the selected records
    # and all this function has to do is filter out the matching
    # company records
    positive_records = []
    for rec in records:
        if rec[3] > 0:  # positive growth means above 0 and does not mean 0
            positive_records.append(rec)
    print_all_records(positive_records)
    print("\nDone finding companies with positive growth.\n\n")


def query_record_by_date(records):
    '''
    query_record_by_date(records):
    This function will ask the user for a date and will search the records
    for the first company who's record states it was founded on this date.
    An error will be given on incorrect date formats.
    If no match is found the user is told that the search found nothing.
    If there is a match then the Company name is given and the Revenue for
    that company.
    '''
    header_text = "Query database by date"
    header_text_size = len(header_text)
    print("*" * (40 - (int(header_text_size/2) + 1)),
          header_text,
          "*" * (40 - (int(header_text_size/2) + 1)))
    print()
    while True:  # this loop will ensure the date format is used
        try:  # we'll use the exception logic to catch bad input
            date_text = input("Query database using a date (dd/mm/yyyy): ")
            date_query = datetime.strptime(date_text, "%d/%m/%Y")
            break
        except ValueError:
            print("Incorrect input. Please follow format: (dd/mm/yyyy)")
    # in order to tell the user that no match was found
    # we need to use a variable to keep track of if we found a match
    match = None
    for rec in records:
        if date_query == rec[6]:  # rec[6] is the date the company is founded
            match = rec
            break
    if match is not None:
        print("Company name:", match[0] + ", Revenue:", match[2])
    else:
        print("No record found for date:", date_query.strftime("%d/%m/%Y"))
    print("\nDone querying by date.\n\n")


def query_total_revenue_by_industry(records):
    '''
    query_total_revenue_by_industry(records):
    This function will calculate the total revenue and the average revenue
    for all companies in the industry specified by the user.
    If no company is part of the industry the user is warned.
    '''
    header_text = "Query database by industry"
    header_text_size = len(header_text)
    print("*" * (40 - (int(header_text_size/2) + 1)),
          header_text,
          "*" * (40 - (int(header_text_size/2) + 1)))
    print()
    total = 0
    companies_in_industry = 0
    while True:  # make sure the user isn't entering blank input
        query_industry = input("Query database using industry: ")
        if len(query_industry) == 0:
            print("Incorrect input. Industry name can not be empty")
        else:
            break
    for rec in records:  # find companies
        if rec[1] == query_industry:  # that match the industry
            total = total + rec[2]  # and add their revenue to the total
            companies_in_industry = companies_in_industry + 1  # add to count
    if companies_in_industry == 0:  # no companies found
        print("No companies are found in your industry:",
              query_industry,
              "\n\n")
        return
    else:
        print("Total revenue (USD billion) for industry",
              query_industry + ":",
              "{:.2f}".format(total))
        print("Average revenue (USD billion) for industry",
              query_industry + ":",
              "{:.2f}".format(total/companies_in_industry))
    print("\nDone querying by industry.\n\n")


def count_companies_between_dates(records):
    '''
    count_companies_between_dates(records):
    This function will ask the user for two dates.
    Then it will count the companies that were founded after the start date
    (the first date the user enters) and were founded before the end date
    (the last date the user enters). The resulting number is then printed out.
    '''
    header_text = "Count companies between dates"
    header_text_size = len(header_text)
    print("*" * (40 - (int(header_text_size/2) + 1)),
          header_text,
          "*" * (40 - (int(header_text_size/2) + 1)))
    print()
    # the following variable start will allow me to reuse the while loop to
    # check whether the user correctly inputs the start date and the end date
    start = 0
    while True:
        if start == 0:
            start_date = input("Please enter start date (dd/mm/yyyy): ")
            try:  # we will again use the exception logic to handle the format
                start_date = datetime.strptime(start_date, "%d/%m/%Y")
                start = 1
                # now that start is 1, I can reuse the loop but not ask
                # the user to re-enter the start date
            except ValueError:
                print("Incorrect input. Must match (dd/mm/yyyy)")
                continue
        end_date = input("Please enter end date (dd/mm/yyyy): ")
        try:
            end_date = datetime.strptime(end_date, "%d/%m/%Y")
            # we will now check that the end_date is later
            # than the start_date and make the user re-enter
            # the values if it doesn't match
            if end_date == start_date:
                print("Incorrect input. Dates must not be the same")
                continue
            if end_date < start_date:
                print("Incorrect input.",
                      "End date must be greater than start date")
                continue
            break
        except ValueError:
            print("Incorrect input. Must match (dd/mm/yyyy)")
    count = 0
    for rec in records:
        # the if statement checks for inclusive matching on the dates
        if rec[6] >= start_date and rec[6] <= end_date:
            count = count + 1
    print("There are",
          count,
          "companies founded between",
          "{d.day}/{d.month}/{d.year}".format(d=start_date),
          "-",
          "{d.day}/{d.month}/{d.year}".format(d=end_date))
    print("\nDone finding companies founded between dates.\n\n")


def write_data(filename, records):
    '''
    write_data(filename, records):
    This function will write out the records to a file given by the parameter
    filename.
    The format of the data written to the file will match the format of the
    data being read by the read_data function.
    '''
    header_text = "Writing data"
    header_text_size = len(header_text)
    print("*" * (40 - (int(header_text_size/2) + 1)),
          header_text,
          "*" * (40 - (int(header_text_size/2) + 1)))
    print()
    # opened with write mode access which will delete the file content first
    # and then allow me to insert new content instead
    with open(filename, 'w') as backup_file:
        for rec in records:
            # each write call will create a new line containing
            # all the fields of the record formatted in such a way
            # as to be identical to the original data.txt file
            backup_file.write(rec[0] +
                              "," +
                              rec[1] +
                              "," +
                              str(int(rec[2])) +
                              "," +
                              "%g" % rec[3] +  # proper float conversion
                              "," +
                              str(rec[4]) +
                              "," +
                              rec[5] +
                              "," +
                              # avoids zero padded dates
                              "{d.day}-{d.month}-{d.year}".format(d=rec[6]) +
                              "\n")
    print("\nDone writing data.\n\n")


def main():
    data = read_data("data.txt")
    print_all_records(data)
    # print_positive_growth(data)
    # query_record_by_date(data)
    # query_total_revenue_by_industry(data)
    count_companies_between_dates(data)
    # write_data("backup.txt", data)


main()
