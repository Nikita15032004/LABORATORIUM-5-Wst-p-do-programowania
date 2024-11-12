#zad 1
def to_square(number):
    return number ** 2
user_number = float(input("Enter a number: "))
result = to_square(user_number)

print(f"The square of {user_number} is: {result}")

#---------------------------------------------------
#zad 2
def reverse_string(text):
    return text[::-1]

user_text = input("Enter a text: ")
result = reverse_string(user_text)
print(f"Original text: {user_text}")
print(f"Reversed text: {result}")


#---------------------------------------------------
#zad 3
def powitanie(imie="Użytkowniku", jezyk="polski"):

    greetings = {
        "polski": f"Cześć, {imie}",
        "angielski": f"Hello, {imie}",
        "niemiecki": f"Guten Morgen, {imie}"
    }
    return greetings.get(jezyk, f"Witaj, {imie}")

print(powitanie())
print(powitanie("Użytkowniku"))
print(powitanie("Amm"))
print(powitanie("John", "angielski"))
print(powitanie("Hans", "niemiecki"))
print(powitanie("Pedro", "wloski"))

#---------------------------------------------------
#zad 4
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

numbers_list = [5, 10, 6, 7]
average = calculate_average(numbers_list)
print(f"Numbers: {numbers_list}")
print(f"Average: {average}")

#---------------------------------------------------
#zad 5
def oblicz_BMI(waga=float(input("Podaj swoja wage w kg")), wzrost=float(input("Podaj swoj wzrost w metrach"))):
    BMI = waga / (wzrost * wzrost)

    if BMI < 18.5:
        return "niedowaga"
    elif 18.5 < BMI < 24.9:
        return "normalna masa ciala"
    elif 25 < BMI < 29.9:
        return "nadwaga"
    elif 30 < BMI < 34.9:
        return "otylosc I stopnia"
    elif 35 < BMI < 39.9:
        return "otylosc II stopnia"
    elif BMI > 40:
        return "otylosc III stopnia"

wynik1 = oblicz_BMI()
print(wynik1)

#---------------------------------------------------
#zad 6
import math
def oblicz_pole_trojkata(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Boki muszą być dodatnie!"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Podane boki nie mogą tworzyć trójkąta!"

    s = (a + b + c) / 2
    pole = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return "Wynik:", pole


try:
    a = float(input("Podaj długość boku a: "))
    b = float(input("Podaj długość boku b: "))
    c = float(input("Podaj długość boku c: "))

    pole = oblicz_pole_trojkata(a, b, c)
    print(f"Pole trójkąta wynosi: {pole:2f}")

except ValueError as e:
    print("Wprodzona wartosc nie jest poprawna")