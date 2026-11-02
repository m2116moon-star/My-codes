#  مقایسه سقوط آزاد روی زمین و ماه
t = np.linspace(0,5, 50)

x_earth = 0.5 * 9.8 * t ** 2
x_moon = 0.5 * 1.6 * t ** 2

plt.plot(t, x_earth, label="زمین", color='blue')
plt.plot(t, x_moon, label="ماه", color='red')

plt.title("مقایسه سقوط آزاد در زمین و ماه")
plt.xlabel("زمان(ثانیه)")
plt.ylabel("مسافت(متر)")
#  نمایش راهنمای رنگ
plt.legend()
plt.grid(True)

plt.show()

#  scatterنمودار نقطه ای
# داده‌های تجربی (مثلاً جرم و کشیدگی فنر)
mass = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
extension = np.array([0.055, 0.092, 0.158, 0.188, 0.255])

# رسم نقطه‌ای
plt.scatter(mass, extension, color='green', marker='o')

plt.title("داده‌های آزمایش فنر")
plt.xlabel("جرم (کیلوگرم)")
plt.ylabel("کشیدگی (متر)")
plt.grid(True)

plt.show()

#  نمایش نمودار سینوس و کسینوس کنار هم
x = np.linspace(0, 5, 100)
y1 = np.sin(x)  #  نمودار اول
y2 = np.cos(x)  #  نمودار دوم

#  ساخت یک شکل با یک ردیف و دو ستون
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

#  نمودار سمت چپ(اندیس صفر)
axes[0].plot(x, y1, color='blue')
axes[0].set_title("نمودار سینوس")
axes[0].set_xlabel("زمان")
axes[0].grid(True)

#  نمودار سمت راست(اندیس1)
axes[1].plot(x, y2, color='red')
axes[1].set_title("نمودار کسینوس")
axes[1].set_xlabel("زمان")
axes[1].grid(True)

#  تنظیم فاصله بین نمودارها
plt.tight_layout()

plt.show()

#  برازش خطی (linear regression)
import numpy as np
import matplotlib.pyplot as plt
#  داده های جرم
mass = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
#  برای k=20 داریم : x = mg / k
extension = (9.8 / 20) * mass
#  تعدادی نویز تصادفی به داده ها اضافه میکنیم تا شبیه آزمایش واقعی شود
noise = np.random.normal(0, 0.005, len(mass))
extension_noisy = extension + noise

#  رسم داده های واقعی 
plt.scatter(mass, extension_noisy, color='green', label="داده های آزمایش")

# ۳. پیدا کردن خط بهترین برازش (درجه ۱ یعنی خط راست)
# این تابع ضرایب شیب و عرض از مبدا را پیدا می‌کند
coefficients = np.polyfit(mass, extension_noisy, 1) 
# coefficients[0] = شیب خط (slope)
# coefficients[1] = عرض از مبدا (intercept)

print("شیب خط:", coefficients[0])
print("عرض از مبدا:", coefficients[1])

#  شیب خط همان g / k  هست.
#  پس اگر  g را بر شیب تقسیم کنیم ثابت فنر بدست میاد
print(9.8 / coefficients[0])

#   ساخت خط بر اساس ضرایب پیدا شده
line = np.polyval(coefficients, mass)

# رسم داده‌ها و خط
plt.scatter(mass, extension_noisy, color='green', label="داده‌های آزمایش")
plt.plot(mass, line, color='red', linewidth=2, label="خط بهترین برازش")

plt.title("برازش خطی داده‌های آزمایش فنر")
plt.xlabel("جرم (کیلوگرم)")
plt.ylabel("کشیدگی (متر)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
#  ذخیره نمودار با فرمت عکس با کیفیت 100
plt.savefig("spring_linear_fit", dpi=100)

plt.show()
