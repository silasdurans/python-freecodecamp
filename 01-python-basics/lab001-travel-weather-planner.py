# Fulfill the user stories below and get all the tests to pass to complete the lab.

distance_mi = 0
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)

elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)

if distance_mi > 1 and distance_mi <= 6:
    if has_bike == True and is_raining == False:
        print(True)
    else:
        print(False)
elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)