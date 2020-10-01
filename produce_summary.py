# Create a file object from .txt so we can access its
 # contents via Python

day_1_file = open("um-deliveries-20140519.txt")
day_2_file = open("um-deliveries-20140520.txt")
day_3_file = open("um-deliveries-20140521.txt")

def melon_summary(day_file, day_num):
    """Print melon report for last three days"""

    print("Day", day_num)
    
    # get each line in file
    for line in day_file:
        line = line.rstrip()    #remove extra whitespace to the right
        words = line.split('|')    #use bar as the delimiter to split line into words

        melon = words[0]    #first index is melon vendor
        count = words[1]    #second index is number of melons sold
        amount = words[2]   #third index is total amount sold

        print("   Delivered {} {}s for total of ${}".format(
        count, melon, amount))
    day_1_file.close()

melon_summary(day_1_file, 1)
print()
print()
melon_summary(day_2_file, 2)
print()
print()
melon_summary(day_3_file, 3)
print()
print()




