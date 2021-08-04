import csv
from collections import Counter

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

data = Counter(new_data)
print(data)

# create a dictionary with range of height as keys and the occurrences of the heights as values which at start is 0
mode_data_for_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}

for height, occurence in data.items():
    # , using if and elif condition we'll check if the height lies between 50-60 ,60-70.70-80.
    # If the height lies in the range the occurrence count will increase
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0

for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [
            int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode = float((mode_range[0] + mode_range[1]) / 2)

print(f"Mode is -> {mode:2f}")
