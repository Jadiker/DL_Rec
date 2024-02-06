import csv

# Data for each file
checkins_data = [
    ["user1", "locationA", "locationB"],
    ["user2", "locationC", "locationA"],
    ["user3", "locationB", "locationD"]
]

locations_list = [["locationA", "locationB", "locationC", "locationD"]]

users_list = [["user1", "user2", "user3"]]

hometowns_data = [
    ["user1", "Hometown1"],
    ["user2", "Hometown2"],
    ["user3", "Hometown3"]
]

# Function to write data to a CSV file
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