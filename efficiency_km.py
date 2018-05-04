PETROL_PRICE_PER_LITRE = 75
distance_travelled = float(input("Enter distance you like to travel in km: "))
amount_paid = float(input("Enter amount paid: "))
fuel_consumed = amount_paid / PETROL_PRICE_PER_LITRE
km_per_litre = distance_travelled / fuel_consumed
print("You can travel %.2f km on a litre of petrol." % km_per_litre)