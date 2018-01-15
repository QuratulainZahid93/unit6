favorite_places = {
    'Aney': ['K2 mountain', 'death valley', 'muree'],
    'Sherry': ['Hocksbay', 'Kappa dopia iceland'],
    'Zain': ['Margilla hills', 'Sawat valley', 'Horse iceland']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())