#  پروژه تحلیل داده های یک آزمایش سقوط آزاد

#  محاسبه زمان نظری سقوط آزاد
import math
ertefa = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
zaman = [1.02,1.43, 1.75, 2.02, 2.26, 2.47, 2.67, 2.86, 3.03, 3.19]

def zaman_soqot_1(h):
    g = 9.8
    t = math.sqrt(2 * h / g)
    return t

t_nazari = []
for h in ertefa:
    t_1 = zaman_soqot_1(h)
    t_nazari.append(t_1)
print(t_nazari)

def khata_1(t, t_n):
    khata_t = abs(t - t_n)
    return khata_t

for i in range(len(zaman)):
    t = zaman[i]
    t_n = t_nazari[i]

#  تابع محاسبه میانگین خطا
def miangin_khata(ertefa, zaman):
    khataha = 0
    n = 0
    for i in range(len(zaman)):
        t_n = zaman_soqot_1(ertefa[i])
        khata = khata_1(zaman[i], t_n)
        khataha += khata
        n += 1
    return khataha / n    

#  تابع بیشترین خطا
def max_khata(ertefa, zaman):
    khata_max = 0
    h_max = 0
    for i in range(len(zaman)):
        t_n_1 = zaman_soqot_1(ertefa[i])
        khata_2 = khata_1(zaman[i], t_n_1)
        if  khata_2 > khata_max:
            khata_max = khata_2
            h_max = ertefa[i]
    return khata_max, h_max

khata_max, h_max = max_khata(ertefa, zaman)
if khata_max == 0:
    print( "همه خظاها صفر هستند")
else:
    print(f"بیشترین خطا در ارتفاع{h_max} = {khata_max}")

# جدول نتایج
def jadval(ertefa, zaman):
    print("خطا | زمان نظری|زمان واقعی|ارتفاع")
    print("-" * 40)
    for i in range(len(zaman)):
        z_s = zaman_soqot_1(ertefa[i])
        khata_0 = khata_1(zaman[i], z_s)
        print(f"  {ertefa[i]}  |   {zaman[i]}    |   {z_s:.3f}   |   {khata_0:.3f}")
jadval(ertefa, zaman)
def save_file(ertefa, zaman):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write("خطا | زمان نظری|زمان واقعی|ارتفاع\n")
        f.write(f"{"-" * 40}\n")
        for i in range(len(zaman)):
            z_s = zaman_soqot_1(ertefa[i])
            khata_0 = khata_1(zaman[i], z_s)
            f.write(f"  {ertefa[i]}  |   {zaman[i]}    |   {z_s:.3f}   |   {khata_0:.3f}\n")

save_file(ertefa, zaman)
