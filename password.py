# Jesteś konsultantem działającym dla Niebezpiecznika - polskiego lidera cyberbezpieczeństwa. Napisz program, który będzie dokonywał audytu bezpieczeństwa u klientów Niebezpiecznika - jesteś odpowiedzialny za moduł sprawdzający złożoność haseł i generujący raport z rekomendacjami. 

# 1. Poproś użytkownika o hasło, a następnie sprawdź, czy spełnia ono reguły bezpieczeństwa.
# 2. Hasło  powinno mieć minimum jedną małą literę, jedną wielką literę i jeden znak specjalny.
# 3. Hasło nie może zawierać spacji!  (wewnętrzny wymóg klienta wynikający z ograniczeń ich systemu teleinformatycznego)
# 4. Hasło musi mieć minimum 8 znaków.
# 5. Jeśli hasło jest niepoprawne, wyświetl raport w punktach co należy zmienić.




# "Twoje hasło jest bezpieczne."
# "Twoje hasło nie jest wystarczająco bezpieczne. Dostosuj się do poniższych reguł: "
# "- twoje hasło powinno składać się z minimum 8 znaków"
# "- twoje hasło NIE może zawierać spacji"
# "- twoje hasło musi zawierać znak specjalny"
# "- twoje hasło musi zawierać małą literę"
# "- twoje hasło musi zawierać wielką literę"






password = input("Podaj hasło: ")

special = 0
lowercase = 0
capital_case = 0

for char in password:
    if not char.isspace() and not char.isalpha() and not char.isdigit():
        special = special + 1
    if char.islower():
        lowercase = lowercase + 1
    elif char.isupper():
        capital_case = capital_case + 1

# print("Twoje hasło ma", lowercase, "małych liter i", capital_case, "dużych.")

if len(password) > 8 and " " not in password and special >= 1 and lowercase > 0 and capital_case > 0:
    print ("Twoje hasło jest bezpieczne.")
else:
    print ("Twoje hasło nie jest wystarczająco bezpieczne. Dostosuj się do poniższych reguł: ")
    if len(password) < 8:
        print ("- twoje hasło musi się składać z minimum 8 znaków")

    if " " in password:
        print("- twoje hasło NIE może zawierać spacji")

    if special == 0:
        print ("- twoje hasło musi zawierać znak specjalny")

    # if password.isalpha() and password.isupper() == True:
    #     print ("- twoje hasło musi zawierać małą literę ") 
    
    if lowercase == 0:
        print ("- twoje hasło musi zawierać małą literę ")

    # if password.isalpha() and password.islower() == True:
    #     print ("- twoje hasło musi zawierać wielką literę ")  
    
    if capital_case == 0:
        print ("- twoje hasło musi zawierać wielką literę ")


