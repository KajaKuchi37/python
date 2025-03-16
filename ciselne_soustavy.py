# převod celých čísel do soustavy se zadaným základem
# Karolína Kučerová, kucerovaka@jirovcovka.net

def convert_to_base(n, base):
    znaky = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    if base < 2 or base > len(znaky):
        raise ValueError("Neplatný základ soustavy")
    
    if n == 0:
        return "0"
    
    negative = n < 0
    n = abs(n)
    result = []
    
    while n > 0:
        result.append(znaky[n % base])
        n //= base
    
    if negative:
        result.append("-")

    return "".join(result[::-1])


with open("vstup.dat", "r", encoding="utf-8") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

base = int(lines[0])
number = int(lines[1])

print(convert_to_base(number, base))