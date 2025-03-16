# práce se seznamem jmen
# Karolína Kučerová, kucerovaka@jirovcovka.net

from collections import Counter

with open("zaci.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file if line.strip()]

krestni_jmena = []
max_pocet_jmen = 0
student_s_nejvice_jmeny = ""

for line in lines:
    parts = line.split()
    krestni_jmena.extend(parts[:-1])  
    format_jmeno = f"{' '.join(f'*{jmeno}*' for jmeno in parts[:-1])} -{parts[-1]}-"
    print(format_jmeno)

    if len(parts) - 1 > max_pocet_jmen: 
        max_pocet_jmen = len(parts) - 1
        student_s_nejvice_jmeny = line

nejcastejsi_jmeno, count = Counter(krestni_jmena).most_common(1)[0]

print("\nNejčastější křestní jméno:", nejcastejsi_jmeno, "(", count, "krát)")
print("Student s nejvíce křestními jmény:", student_s_nejvice_jmeny, "(", max_pocet_jmen, "jména)")