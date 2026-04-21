# Package
weight = 40

# Shipment cost for ground shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20
  print(f"Ground shipping costs ${round(cost_ground,2)}")
elif weight <= 6:
  cost_ground = weight * 3 + 20
  print(f"Ground shipping costs ${round(cost_ground,2)}")
elif weight <= 10:
  cost_ground = weight * 4 + 20
  print(f"Ground shipping costs ${round(cost_ground,2)}")
else:
  cost_ground = weight * 4.75 + 20
  print(f"Ground shipping costs ${round(cost_ground,2)}")

# Shipment cost for premium shipping
cost_premium_ship = 125
print(f"Ground Shipping Premium costs ${cost_premium_ship}")

# Shipment cost for drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50
  print(f"Drone shipping costs ${round(cost_drone,2)}")
elif weight <= 6:
  cost_drone = weight * 9
  print(f"Drone shipping costs ${round(cost_drone,2)}")
elif weight <= 10:
  cost_drone = weight * 12
  print(f"Drone shipping costs ${round(cost_drone,2)}")
else:
  cost_drone = weight * 14.25
  print(f"Drone shipping costs ${round(cost_drone,2)}")
print("-----------------------------------")

cheapest_cost = min(cost_ground, cost_premium_ship, cost_drone)
if cheapest_cost == cost_ground:
    cheapest_way = "Ground shipping costs"
    print(f"The cheapest way of shipment is '{cheapest_way}' which costs ${round(cheapest_cost,2)}")
elif cheapest_cost == cost_premium_ship:
    cheapest_way = "Ground Shipping Premium"
    print(f"The cheapest way of shipment is '{cheapest_way}' which costs ${round(cheapest_cost,2)}")
else:
    cheapest_way = "Drone shipping costs"
    print(f"The cheapest way of shipment is '{cheapest_way}' which costs ${round(cheapest_cost,2)}")