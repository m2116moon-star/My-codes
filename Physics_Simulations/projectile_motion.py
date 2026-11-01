# پروژه شبیه سازی پرتابه با در نظرگرفتن مقاومت هوا
import numpy as np
#  پارامترهای اولیه
v0 = 30
teta = 45
g = 9.8
t_max = 10
#  گامهای زمانی
dt = 0.01
#  ضریب مقاومت هوا
k_air = 0.05

#  تابع شبیه سازی حرکت پرتابه
def shabih_sazi_partabe(v0, teta, dt, t_max, k_air):
    t = np.arange(0, t_max + dt, dt)
    #  سرعت ها
    v_x = v0 * np.cos(np.deg2rad(teta))
    v_y = v0 * np.sin(np.deg2rad(teta))
    bord = []
    ertefa = []
    #  مکان اولیه پرتابه
    x =0
    y = 0
    #  اگر حلقه کامل شود و توپ به زمین برخورد نکند زمان پایان همان زمان ماکس است
    t_payan = t_max
    for i in range(len(t)):
        #  در هر دور از حلقه مکانهای جدید به لیست اضافه میشوند
        bord.append(x)
        ertefa.append(y)
        #  هرگاه توپ به زمین برخورد کند حلقه متوقف میشود
        if y < 0:
            t_payan = i * dt
            break
            
        #  به روز رسانی شتاب ها
        a_x = -k_air * v_x
        a_y = -g - k_air * v_y
        #  به روز رسانی سرعت ها
        v_x = v_x + a_x * dt
        v_y = v_y + a_y * dt
        #  به روز رسانی مکان ها
        x = x + v_x * dt
        y = y + v_y * dt
        
    return x, y, t_payan, bord, ertefa    

#  اجرای تابع
x_payan, y_payan, t_payan, bord, ertefa = shabih_sazi_partabe(v0, teta, dt, t_max, k_air)
print(f" برد : {x_payan:.2f}, زمان پایانی : {t_payan}")

#  تحلیل نتایج
bord_arr = np.array(bord)
ertefa_arr = np.array(ertefa)
max_h = np.max(ertefa_arr)
print(f" برد : {np.max(bord_arr):.2f}")
print(f" بیشترین ارتفاع : {max_h:.2f}")

#  مقایسه برد پرتابه درحضور مقاومت هوا و بدون مقاومت هوا
x_05, y_05, t_05, bord_05, ertefa_05 = shabih_sazi_partabe(v0 =30, teta = 45, dt = 0.01, t_max = 10, k_air = 0.05)
print(f" برد با مقاومت 0.05 : {x_05:.2f} متر , در مدت زمان : {t_05:0.2f} ثانیه ")

x_0, y_0, t_0, bord_0,ertefa_0 = shabih_sazi_partabe(v0 =30, teta = 45, dt = 0.01, t_max = 10, k_air = 0)
print(f"برد بدون مقاومت : {x_0:.2f} متر , در مدت زمان : {t_0:0.2f} ثانیه ")

def save_to_file(x, t, max_h):
    with open("natayej.txt", "w", encoding="utf-8") as f:
        f.write("===نتایج شبیه سازی حرکت پرتابه===\n")
        f.write(f" زمان پرواز : {t_payan:.2f}\n")
        f.write(f" برد پرتابه : {x_payan:.2f}\n")
        f.write(f" بیشترین ارتفاع : {max_h:.2f}\n")

save_to_file(x_payan, t_payan, max_h)

import matplotlib.pyplot as plt
#  رسم نمودار
plt.plot(bord, ertefa)
plt.xlabel("برد(متر)")
plt.ylabel("(متر)ارتفاع")
plt.title("مسیر حرکت پرتابه با مقاومت هوا")
plt.grid(True)
plt.show()

#  برای تغییر فاصله گریدها وارد میکنیم
from matplotlib.ticker import MultipleLocator

#  ساخت یک شکل با یک ردیف و دو ستون
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

#  نمودار سمت چپ(اندیس صفر)
x1 = bord_0
y1 = ertefa_0
axes[0].plot(x1, y1, color='blue')
axes[0].set_title("مسیر حرکت پرتابه بدون مقاومت هوا")
axes[0].set_xlabel("(متر)برد")
axes[0].set_ylabel("(متر)ارتفاع")
axes[0].grid(True)

#  نمودار سمت راست(اندیس1)
x2 = bord_05
y2 = ertefa_05
axes[1].plot(x2, y2, color='red')
axes[1].set_title("مسیر حرکت پرتابه با مقاومت 0.05")
axes[1].set_xlabel("(متر)برد")
axes[1].set_ylabel("(متر)ارتفاع")
axes[1].grid(True)
#  رعایت فاصله بین نمودارها
plt.tight_layout()

# برای نمودار سمت چپ (آبی)
axes[0].xaxis.set_major_locator(MultipleLocator(10))  # خطوط عمودی هر ۱۰ واحد
axes[0].yaxis.set_major_locator(MultipleLocator(2))   # خطوط افقی هر ۲ واحد

# برای نمودار سمت راست (قرمز)
axes[1].xaxis.set_major_locator(MultipleLocator(10))
axes[1].yaxis.set_major_locator(MultipleLocator(2))


# تنظیم محدوده‌ی یکسان برای هر دو نمودار
axes[0].set_xlim(0, 100)
axes[1].set_xlim(0, 100)

axes[0].set_ylim(0, 25)
axes[1].set_ylim(0, 25)

#  برای تبدیل گرید به نقطه چین
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[1].grid(True, linestyle='--', alpha=0.6)

#  ذخیره نمودار با فرمت عکس با کیفیت 100
plt.savefig("projectile_motion", dpi=100)

plt.show()


