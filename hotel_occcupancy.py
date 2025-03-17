"""
Matthew Anderson - 16 March 2025
"""

## Get the number of floors as an integer > 0

floors = -1
while floors == -1:
    floor_input = int(input("Enter the number of floors: "))
    if floor_input > 0:
        floors = floor_input
    else:
        print("Invalid number of floors.")

total_rooms = 0
total_ocupied_rooms = 0

for floor in range(1, floors+1):

    ## get the number of rooms as an integer greater than zero

    rooms = -1
    while rooms == -1:
        room_input = int(input(f'[Floor {floor}] Enter the total number of rooms: '))
        if room_input > 0:
            rooms = room_input
        else:
            print("Invalid number of rooms.")

    ocupied_rooms = -1
    while ocupied_rooms == -1:
        ocupied_room_input = int(input(f'[Floor {floor}] Enter the number of ocupied rooms: '))
        ## make sure that the number of occupied rooms is between 0 and the total rooms on the floor
        if ocupied_room_input >= 0 and ocupied_room_input <= rooms: 
            ocupied_rooms = ocupied_room_input
        else:
            print("Invalid number of ocupied rooms.")

    occupancy_rate = ocupied_rooms / rooms;

    total_rooms += rooms
    total_ocupied_rooms += ocupied_rooms

    print(f'\n{"-" * 40}')
    print(f'Floor {floor}: {rooms} room(s), {ocupied_rooms} ocupied.')
    print(f'The ocupancy rate for floor {floor} is {occupancy_rate:.2f}')
    print(f'{("-" * 40)}\n')


vacant_rooms = total_rooms - total_ocupied_rooms
overall_occupancy_rate = total_ocupied_rooms / total_rooms

print(f'{"-" * 12} Hotel Overview {"-" * 12}')
print(f'The hotel has {total_rooms} room(s).')
print(f'{total_ocupied_rooms} of the rooms were ocupied.')
print(f'{vacant_rooms} of the rooms were vacant.')
print(f'The overall occupancy rate for the hotel is {overall_occupancy_rate:.2f}')
