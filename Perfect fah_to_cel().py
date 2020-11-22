def fah_to_cel(start, end, step): # version 2
    print(f"{'Fahrenheit':>12}{'Celcius':>12}")
    print(f"{'----------':>12}{'-------':>12}")
    fah = start
    if start < end and step < 0:
        print("  ----------     -------")
    elif start > end and step > 0:
        print("  ----------     -------")
    elif start < end:
        while fah < end:
            cel = (5 / 9) * (fah - 32)
            print(f"{fah:12.2f}{cel:12.2f}")
            fah = fah + step
        print(f"{'----------':>12}{'-------':>12}")
    elif start > end:
        while fah > end:
            cel = (5 / 9) * (fah - 32)
            print(f"{fah:12.2f}{cel:12.2f}")
            fah = fah + step
        print(f"{'----------':>12}{'-------':>12}")


fah_to_cel(15, 20, -1)