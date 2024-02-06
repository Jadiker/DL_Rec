import csv

# Corrected and expanded data for each file
checkins_data = [
    ["userA", "location1", "location2", "location3", "location4", "location5", "location6", "location7", "location8"],
    ["userB", "location4", "location5", "location6", "location7", "location8", "location9", "location10", "location11"],
    ["userC", "location8", "location9", "location10", "location11", "location12", "location13", "location14", "location15"],
    ["userD", "location16", "location17", "location18"],
    ["userE", "location19", "location20", "location21"],
    ["userF", "location22", "location23", "location24"],
    ["userG", "location25", "location26", "location27"],
    ["userH", "location28", "location29", "location30"],
    ["userI", "location31", "location32", "location33"],
    ["userJ", "location34", "location35", "location36"]
]

# Adjusting the locations list to include 36 locations now
locations_list = [["location" + str(i) for i in range(1, 37)]]

# Users list remains the same
users_list = [["user" + chr(65 + i) for i in range(10)]]

# Hometowns data remains the same
hometowns_data = [
    ["userA", "HometownA"],
    ["userB", "HometownB"],
    ["userC", "HometownC"],
    ["userD", "HometownD"],
    ["userE", "HometownE"],
    ["userF", "HometownF"],
    ["userG", "HometownG"],
    ["userH", "HometownH"],
    ["userI", "HometownI"],
    ["userJ", "HometownJ"]
]

# Function to write data to a CSV file remains the same
def write_to_csv(file_name, data):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Write each dataset to its respective file
write_to_csv('data/checkins.csv', checkins_data)
write_to_csv('data/locationsList.csv', locations_list)
write_to_csv('data/usersList.csv', users_list)
write_to_csv('data/hometownsMultiLine.csv', hometowns_data)
print("Data generated successfully!")