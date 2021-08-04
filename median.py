import csv

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

# remove the title list from the data
file_data.pop(0)


# sorting data  to get the height of people.
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

#length of the data
#The length is to check if the number of values in the data are even or not
n = len(new_data)

#sort the data in ascending order
new_data.sort()

#using floor division to get the nearest number whole number
# floor division is shown by //

#If the length is an even number then there will be 2 values as medians and we'll have to find the mean of those two values
if n % 2 == 0:
    #getting the first number
	median1 = float(new_data[n//2])
    #getting the second number
	median2 = float(new_data[n//2 - 1])
    #getting mean of those numbers
	median = (median1 + median2)/2

#If the length is a odd number then get the middle number is median
else:
    median = new_data[n//2] 


print("Median is: " + str(median))
