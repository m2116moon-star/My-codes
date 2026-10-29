#   واپاشی ماده رادیو اکتیو و نیمه عمر
t_2 = np.linspace(0, 10, 21)
N0 = 1000
lambd = 0.3
N = N0 * np.exp(-lambd * t_2)
print(np.min(N))
print(np.max(N))
#  زمان نیمه شدن مقدار ماده = نیمه عمر
#  N(t) = N0 * exp(-lambd * t) = N0 / 2
# lambd * t = ln 2
# t_haf = ln 2 / lambd
#  نکته: ln = np.log
print(np.log(2) / lambd)

#  نوسانگر
t = np.linspace(0, 2, 50)
A = 2
f = 1
x = A * np.cos(np.pi * 2 * f * t)
print(np.min(x))
print(np.max(x))
print(np.mean(x))

#  موج
k = 2 * np.pi
x = np.linspace(0, 2, 100)
y = np.sin(k * x)
print(np.sum(y))

#  نوسانگر میرا
A = 1
gama = 0.3
omega = 2 * np.pi
t = np.linspace(0, 10, 100)
x = A * np.exp(-gama * t) * np.cos(omega * t)
print(np.min(x))
print(np.max(x))
print(np.max(np.abs(x)))

#  حل معادله
#  3x + 2y = 12
#  x - y = 1
A = np.array([[3, 2],
             [1, -1]])
B = np.array([12, 1])
print(np.linalg.solve(A, B))

# پیدا کردن جریان در مدار مقاومتهای موازی
#  10 * i_1 + 20 * i_2 = 100
#  i_1 - i_2 = 0
A = np.array([[10, 20], [1, -1]])
B = np.array([100, 0])
print(np.linalg.solve(A, B))

#  محاسبه عدد پی با اعداد تصادفی! 
#  تعداد نقاط درون مربع
N = 100000
x = np. random.rand(N)
y = np.random.rand(N)

inside = x ** 2 + y ** 2 <= 1
n_inside = np.sum(inside)

p_est = 4 * n_inside / N

print(f" pi_takhmini : {p_est:.4f}")
print(f" np.pi  : {np.pi:.4f}")

#  شبیه سازی واپاشی هسته ای
import numpy as np
N0 = 1000
p = 0.01
t_max = 100

N = N0
for t in range(t_max):
    #  احتمال واپاشی برای هر اتم یک عدد بین صفر و یک هست
    decays = np.random.rand(N) < p
    N -= np.sum(decays)
print(f" اتمهای باقیمانده: {N}")
print(f" انتظار تیوری:{N0 * np.exp(-p * t_max):.0f}")

#  میانگین با مونت کارلو
# میانگین با فرمول تحلیلی : انتگرال تقسیم بر بازه
N = 100000
x = np.random.rand(N)
f = x ** 2
mean_est = np.mean(f)
print(f" میانگین تخمینی :{mean_est:.4f}")
print(f" میانگین واقعی:{1 / 3:.4f}")

#  شبیه سازی پرتاب سکه
N = 1000
result = np.random.randint(0, 2, N)
shir = np.sum(result == 1)
khat = np.sum(result ==0)

print(f"shir : {shir}")
print(f"khat : {khat}")
print(f"{shir / N * 100 :.2f}: درصد شیر")

#  پرتاب تاس
N = 1000
n = np.random.randint(1, 7 ,N)
n_1 = np.sum(n == 1)
n_2 = np.sum(n ==2)
n_3 = np.sum(n ==3)
n_4 = np.sum(n == 4)
n_5 = np.sum(n ==5)
n_6 = np.sum(n ==6)

print(f" 1:{n_1}  2:{n_2}  3:{n_3}  4:{n_4}  5:{n_5}  6:{n_6}")

