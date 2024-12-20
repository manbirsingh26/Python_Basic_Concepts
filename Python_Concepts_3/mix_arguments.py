def mix(a, b, c, d=10, *args, **kwargs):
    print(a, b, c)
    print(d)
    print(args)
    print(kwargs)
    return 0
mix(2, 4, 6)
mix(2.5, 5, 7.5, 15, "A", "B", "C", "D", "E", Name="Kashyap", Address="Sanjay Nagar", Profession="Teaching")

