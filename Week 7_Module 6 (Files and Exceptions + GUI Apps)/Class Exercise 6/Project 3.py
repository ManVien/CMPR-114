# Project 3 (Writing and reading the Sales Data)

def sales():

    num_days = int(input('enter the days of sales: '))
    sales_file = open('sales.txt','a')

    for count in range(1,num_days + 1): # start with 1, and increment by 1 based on the input
        # inside of the loop because its nested after the for loop
        sales = float(input('enter the sales for day # ' + str (count) + ' : '))
        sales_file.write(str(sales) + '\n')

    # outside of the loop, by indenting
    sales_file.close()
    print('sales recorded.')

sales()

def ReadSales():

    sales_file = open('sales.txt','r')

    line = sales_file.readline()

    while line != '': # as long as an empty string is NOT returned
        amount = float(line)
        print(format(amount, '.2f'))
        line = sales_file.readline()

    sales_file.close()

ReadSales()
