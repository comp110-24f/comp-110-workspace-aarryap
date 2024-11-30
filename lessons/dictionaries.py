"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}
ice_cream["strawberry"] = 5

ice_cream["mint"] = 3

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint ice cream.")

ice_cream.pop("strawberry")

for key in ice_cream:
    print(key + " has " + str(ice_cream[key]) + " orders.")
