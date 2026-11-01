import numpy as np
import matplotlib.pyplot as plt
# شبیه سازی داده های یک سنسور نویز دار(دمای واقعی حدود 25 درجه)
#  این خط موجب می شود نقاط تصادفی که بعدا تولید میکنیم برای افراد مختلفی که از این کد استفاده میکنند یکسان باشد و نتیجه آزمایش یکسان شود
np.random.seed(42)
zaman = np.arange(0, 50)
#  سیگنال واقعی
dama_vaghe = 25 + 2 * np.sin(zaman / 5)
#  نویز تصادفی
noise = np.random.normal(0, 1.5, 50)
#  سیگنالی که سنسور ثبت کرده
dama_sensor = dama_vaghe + noise

#  اجرای پروژه
# رسم نمودار برای داده های خام
plt.plot(zaman, dama_sensor, color='red', marker='o')
plt.title("داده های خام")
plt.xlabel("زمان")
plt.ylabel("دمای سنسور")
plt.grid(True)

plt.show()
#  محاسبه میانگین و انحراف معیار
print(f" میانگین: {np.mean(dama_sensor)}")
print(f" انحراف معیار: {np.std(dama_sensor)}")

#  مرحله حذف نویز(فیلتر کردن)
dama_filter_shode = []
for i in range(1, len(dama_sensor)-1):
    majmoo = dama_sensor[i-1] + dama_sensor[i] + dama_sensor[i+1]
    dama_filter_shode.append(majmoo / 3)

#  در اینجا دو عضو اول و آخر از داده ها حذف میشوند.بنابراین برای رسم نمودار باید دو زمان متناظر(اول و آخر) را هم حذف کنیم
#  zaman_filter_shode = zaman[1:-1]

dama_filter_shode = np.array(dama_filter_shode)

#  رسم نمودار مقایسه ای(داده های خام و داده های فیلتر شده)
zaman_filter_shode = zaman[1:-1]
dama_filter_shode = np.array(dama_filter_shode)
plt.scatter(zaman, dama_sensor, color='red', alpha=0.4, label=" سیگنال خام(نویز دار)")

plt.plot(zaman_filter_shode, dama_filter_shode, color='blue', linewidth=2, label="سیگنال فیلتر شده")

plt.title("مقایسه دو نمودار سیگنال نویز دار با سیگنال فیلتر شده")
plt.xlabel("زمان(ثانیه)")
plt.ylabel("دما(درجه سانتیگراد)")
plt.legend()
plt.grid(True)

plt.savefig(" نمودار حذف نویز", dpi=100)
plt.show()

print(f" انحراف معیار: {np.std(dama_filter_shode)}")

