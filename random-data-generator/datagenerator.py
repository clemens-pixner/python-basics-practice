import random
names = []
first_name = ["Luca", "James", "Sofia", "Kenji", "Amina", "Matej", "Léa", "Diego", "Noor", "Elias"]
last_name = ["Rossi", "Müller", "García", "Novak", "Dubois", "Silva", "Kowalski", "Andersson", "Petrov", "Hassan"]
country = ["Italien", "Deutschland", "Spanien", "Frankreich", "Japan", "Portugal", "Polen", "Schweden", "Ägypten", "Kanada"]
area_code = {
    "Italy" : "+39",
    "Germany" : "+49", 
    "Spain" : "+34", 
    "France" : "+33", 
    "Japan" : "+81", 
    "Portugal" : "+351", 
    "Poland" : "+48", 
    "Sweden" : "+46",
    "Egypt" : "+20", 
    "Canada" : "+1"
}
while True:
    try:
        amount = int(input("How many identities do you want to create? "))
        break
    except ValueError:
        print("Please enter a valid number")
        continue 
first_names_random = random.sample(first_name, amount)
last_names_random = random.sample(last_name, amount)

for i in range(amount):
    print(f"{first_names_random[i]} {last_names_random[i]}")
  