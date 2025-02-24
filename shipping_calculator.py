import math

shipping_type = input("Shipping type (ocean/air/ground): ")
package_weight = float(input("Package weight (lb): "))
distance_shipped = float(input("Distance (mi): "))

total_cost = 0

## Account for base fee
if shipping_type == "ocean":
    total_cost += 4.99

elif shipping_type == "air":
    total_cost += 6.99

elif shipping_type == "ground":
    total_cost += 2.99

compensated_weight = package_weight - 2
additional_factor = math.ceil(compensated_weight/2) * math.ceil(distance_shipped/500)

if compensated_weight <= 2:
    # For packages less than 2 pounds, the total shipping charge is the base charge no matter how many miles shipped
    total_cost += math.ceil(compensated_weight/2) * 1.10

elif compensated_weight <= 6:
    total_cost += additional_factor * 2.20

elif compensated_weight <= 10:
    total_cost += additional_factor * 3.70

else:
    total_cost += additional_factor * 3.80

print(f'\nTotal Cost: ${total_cost:.2f}')