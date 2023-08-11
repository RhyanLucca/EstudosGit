import time

x = 999

cont=1


while cont <=x:

    if cont == 1:
        print(f"LÁ ELE! {cont} VEZ!")
        cont += 1
        time.sleep(0.03)
    else:
        print(f"LÁ ELE! {cont} VEZES!")
        cont += 1
        time.sleep(0.03)

print("LÁ ELE 1000 VEZES!!!")
time.sleep(3)