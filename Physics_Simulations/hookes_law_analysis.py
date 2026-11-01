import math
mass = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]   #  داده های جرم وزنه
extension = [0.055, 0.092, 0.158, 0.188, 0.255, 0.287, 0.355, 0.385, 0.452, 0.485]    #  داده های میزان کشیدگی فنر

def niroo(m):           #  محاسبه نیروی کشش فنر
    g = 9.8
    return m * g

def sabet_fanar(m, x):         #  محاسبه ثابت فنر برای هر جرم و کشیدگی
    f = niroo(m)
    return f / x

def miangin_k(mass, extension):         #  k تابع میانگین 
    tot = 0
    for i in range(len(mass)):
        tot += sabet_fanar(mass[i], extension[i])
    return tot / len(mass)

def enheraf_meyar(mass, extension):          #   تابع انحراف معیار
    import math
    k_ave = miangin_k(mass, extension)
    y = 0
    for i in range(len(mass)):
        k_i = sabet_fanar(mass[i], extension[i])
        y += (k_i - k_ave) ** 2
    return math.sqrt(y / len(mass))   

def max_khata(mass, extension):           #   تابع بیشترین خطا برای کدام جرم
    khata_max = 0
    mass_of_max = 0
    k_ave = miangin_k(mass, extension)
    for i in range(len(mass)):
        k_i = sabet_fanar(mass[i], extension[i])
        khata = abs(k_i - k_ave)
        if khata > khata_max:
            khata_max = khata
            mass_of_max = mass[i]
    return khata_max, mass_of_max      

def jadval(mass, extension):            #   تابع جدول
    print(" خطا| ثابت فنر| نیرو |  جرم")
    print("-" * 40)
    k_ave = miangin_k(mass, extension)
    for i in range(len(mass)):
        m = mass[i]
        f = niroo(mass[i])
        k_i = sabet_fanar(mass[i], extension[i])
        khata = abs(k_i - k_ave)
        print(f"{m:6.2f}|{f:7.2f}|{k_i:9.2f}|{khata:6.2f}")
    e = enheraf_meyar(mass, extension)
    kh_max, mass_max = max_khata(mass, extension)
    print("-" * 40)
    print("میانگین خطا =", k_ave)
    print("انحراف معیار =", e )
    print(f"بیشترین خطا ={kh_max:.3f} , جرم بیشترین خطا ={mass_max:.3f}")

jadval(mass, extension)

def save_to_file(mass, extension):
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write(" خطا| ثابت فنر| نیرو |  جرم\n")
        f.write(f"{"-" * 40}\n")
        k_ave = miangin_k(mass, extension)
        for i in range(len(mass)):
            m = mass[i]
            f_n = niroo(mass[i])
            k_i = sabet_fanar(mass[i], extension[i])
            khata = abs(k_i - k_ave)
            f.write(f"{m:6.2f}|{f_n:7.2f}|{k_i:9.2f}|{khata:6.2f}\n")    
        e = enheraf_meyar(mass, extension)
        kh_max, mass_max = max_khata(mass, extension)
        f.write(f"{"-" * 40}\n")
        f.write(f"میانگین خطا = {k_ave}\n")
        f.write(f"انحراف معیار = {e}\n" )
        f.write(f"بیشترین خطا ={kh_max:.3f} , جرم بیشترین خطا ={mass_max:.3f}\n")

save_to_file(mass, extension)
