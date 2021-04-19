#-*-coding: utf-8-*-
import matplotlib.pyplot as plt
import numpy as np

iteration = 0
start_k = 178
# Призводительность цеха 1
def f1(x):
    return 6+np.log(x)+8

# Призводительность цеха 2
def f2(x):
    return np.log(x)+10 

# Общая производительность за месяц
def w(k, x):
    return (f1(x)+f2(k-x))

# Остаток производства за месяц
def phi(k,x):
    return (0.65 *x + 0.87*(k-x))

# Вычисление условного оптимального выигрыша при заданном остатке k
def  W(k,ks,Ws):
    xs =  np.arange(k+1)
    next_k = phi(k,xs)
    vals = w(k,xs) + Ws[np.searchsorted(ks,next_k)]
    besti = np.argmax(vals)
    return (vals[besti],xs[besti])

# Вычисление условного оптимального выигрыша при заданном остатке k и заданных
# управлениях xs.
def Wx(k, xs, ks, Ws):
    next_k = phi(k, xs)
    return w(k,xs) + Ws[np.searchsorted(ks, next_k)]

#Для  3-го месяца
print("3 месяц")
k_4 = np.linspace(0.65**3*178,0.87**3*178,10)
W_4 = np.zeros(len(k_4)+1)
k3_min = 0.65**2*178
k3_max = 0.87**2*178
k_3 = np.linspace(k3_min,k3_max,10)
#W_3 = np.zeros(len(k_4)+1)
W_3 = np.zeros(len(k_4))
x_3 = W_3
for i in range(len(k_3)):
    (W_3[i],x_3[i]) = W(k_3[i],k_4,W_4)

print("k_3:",k_3)
print("x_3:",x_3)
plt.plot(k_3,x_3)
plt.xlabel('k_3')
plt.ylabel('x_3')
plt.grid(True)
plt.title('График функции k_3,x_3')
plt.show()
    
x3_min = np.arange(0,k3_min,5)
x3_max = np.arange(0,k3_max,5)
W_3 = np.linspace(np.max(w(k3_min,x3_min)),np.max(w(k3_max,x3_max)),11)
plt.plot(x3_max,w(k3_max,x3_max),x3_min,w(k3_min,x3_min))
plt.xlabel('x')
plt.ylabel('W_3')
plt.grid(True)
plt.title('Графики функций W_3(k3_max,x3_max) и W_3(k3_min,x3_min)')
plt.show()

#Для  2-го месяца
print("2 месяц")
k2_min = 0.65**1*178
k2_max = 0.87**1*178
k_2 = np.linspace(k2_min,k2_max,10)
#W_2 = np.zeros(len(k_2)+1)
W_2 = np.zeros(len(k_2))
x_2 = W_2
for i in range(len(k_2)):
    (W_2[i],x_2[i]) = W(k_2[i],k_3,W_3)

print("k_2:",k_2)
print("x_2:",x_2)
plt.plot(k_2,x_2)
plt.xlabel('k_2')
plt.ylabel('x_2')
plt.grid(True)
plt.title('График функции k_2,x_2')
plt.show()
    
x2_min = np.arange(k2_min)
x2_max = np.arange(k2_max)
w2_max = Wx(k2_max, x2_max, k_3, W_3);
w2_min = Wx(k2_min, x2_min, k_3, W_3);
W_2 = np.linspace(np.max(w2_min),np.max(w2_max),11)
plt.plot (x2_max,w2_max,x2_min,w2_min);
plt.xlabel('x')
plt.ylabel('W_2')
plt.grid(True)
plt.title('Графики функций W_2(k2_max,x2_max) и W_2(k2_min,x2_min)')
plt.show()

#Для  1-го месяца
k1_max = 178
x1_max = np.arange(k1_max)
k_1 = np.linspace(0.65**0*178,0.87**0*178,10)
W_1 = np.zeros(len(k_1)+1)
x_1 = W_1
for i in range(len(k_1)):
     (W_1[i],x_1[i]) = W(k_1[i],k_2,W_2)
w1_max = Wx(k1_max,x1_max,k_2,W_2)
W_1 = np.max(w1_max)

plt.plot(x1_max,w1_max)
plt.xlabel('x')
plt.ylabel('W_3')
plt.grid(True)
plt.title('Графики функций W_1(k1_max,x1_max) и W_1(k1_min,x1_min) совпадают')
plt.show()

print("Total Win W1= ",W_1)
print("k_1:",k_1)
print("x_1:",x_1)
