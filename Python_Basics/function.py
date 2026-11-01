#  تابع جدول ضرب
def jadval_zarb(a):
    for n in range(1,11):
        print(f"{n}*{a}={n*a}")

#  تبدیل سانتیگراد به فارنهایت
def C_to_F(C):
    F=C*1.8+32
    return F
#  تبدیل فارنهایت به سانتیگراد
def F_to_C(F):
    return(F-32)/1.8

#  تابع عدد اول
def adad_aval(n):
    if n < 2:
        return "not aval"    
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return "not aval"
    return "aval"
    
#  محاسبه فاکتوریل
def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac

#  میانگین متحرک
def miangin_motoharek(num):
    for i in range(len(num) - 2):
        majmoo = num[i] + num[i + 1] + num[i + 2]
        print(majmoo / 3)

#  انرژی جنبشی
def energy_kenetic(m,v):
    e = 0.5 * m * v ** 2
    return(e)
    
#  محاسبه سرعت و مسافت جسم درحال سقوط در هر لحظه
def jadval_soqot(t_max):
    g = 9.8
    for t in range(0, t_max + 1):
        v = g * t
        x = 0.5 * g * t ** 2
        print(f"t={t}s | v={v:.2f}m/s | x={x:.2f}m")
        
# ایا جسم به سرعت ماکس میرسد و در چه زمانی
def soqot(v0,v_max):
    g = 9.8
    for t in range(0,30):
        v = g * t + v0
        if v >= v_max:
            return(f"arrived in {t} s")
    return(f"not arrived")    
    
#  تابع روی لیست
# تابعی که بیشترین مقدار لیست را برمیگرداند
def bozorgtarin(liste):
    if len(liste) == 0:
        return None
    bozorg = liste[0]   # فرض کن اولی بزرگترین است
    for x in liste:
        if x > bozorg:
            bozorg = x   # هرجا بزرگتر پیدا کردی به روزرسانی کن
    return bozorg        

# کوچکترین و بزرگترین
def kamtar_bishtar(list):
    if len(list) == 0:
        return None
    kamtar = list[0]
    bishtar = list[0]
    for z in list:
        if z < kamtar:
            kamtar = z
        if z > bishtar:
            bishtar = z
    return (kamtar, bishtar)

#  شمارش اعداد زوج
def tot_zoj(list_1):
    i = 0
    for n in list_1:
        if n % 2 == 0:
            i += 1
    if i == 0:
        return None
    return i       


