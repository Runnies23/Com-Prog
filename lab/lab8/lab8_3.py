
def fah_to_cel(start,end,step):
    if (start > end and step > 0)or (start < end and step < 0):
        print(f"{'Fahrenheit':>12}{'Celcius':>12}")
        print(f"{'----------':>12}{'-------':>12}")
        print(f"{'----------':>12}{'-------':>12}")
        return 
    
    print(f"{'Fahrenheit':>12}{'Celcius':>12}")
    print(f"{'----------':>12}{'-------':>12}")
    fah = start

    # for fah in range(start,end,step):
    if start > end:
        while fah > end:
            cel = (5/9)*(fah-32)
            print(f"{fah:12.2f}{cel:12.2f}")
            fah = fah + step
        print(f"{'----------':>12}{'-------':>12}")

    else:
        while fah < end:
            cel = (5/9)*(fah-32)
            print(f"{fah:12.2f}{cel:12.2f}")
            fah = fah + step
        print(f"{'----------':>12}{'-------':>12}")

fah_to_cel(15,20,1)
fah_to_cel(20,15,-1)
fah_to_cel(15,20,-1)
fah_to_cel(20,15,1)
fah_to_cel(1,5,.3)
