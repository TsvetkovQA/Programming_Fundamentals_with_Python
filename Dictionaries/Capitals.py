country = input().split(", ")
capital = input().split(", ")

information = dict(zip(country, capital))
for country, capital in information.items():
    print(f"{country} -> {capital}")
