validCurrencies = ["EUR","GBP","USD","JPY"]

#welcome message
print("************************************")
print("****          PETERS            ****")
print("****     CURRENCY CONVERTER     ****")
print("****                            ****")
print("************************************")
print("")
print("List of currencies: ")
print("  GBP - British Pound £")
print("  EUR - Euro €")
print("  USD - US Dollar $")
print("")

#variables initialised
currencyFrom = ""
currencyTo = ""
amount = 0

#gbp exchange rate variables
gbp_eur = 1.17687
gbp_usd = 1.28922

#eur exchange rate variables
eur_gbp = 0.851460
eur_usd = 1.09678

#usd exchange rate variables
usd_gbp = 0.776378
usd_eur = 0.911640


#convesion from one currency to another
def converter(amount,modifier):
  answer = amount * modifier
  answer = str(answer)
  answer = answer[:5]
  return answer

while True:


  #ask for user to input answers
  while not currencyFrom in validCurrencies:
    currencyFrom = input("Enter Currency to convert From: ").upper()
    
  while not currencyTo in validCurrencies:
    currencyTo = input("Enter Currency to convert To: ").upper()

  amount = float(input("Enter amount to convert: "))


  #gbp currencies
  if currencyFrom == "GBP" and currencyTo == "EUR":
    print("You get: €" + converter(amount,gbp_eur))

  if currencyFrom == "GBP" and currencyTo == "USD":
    print("You get: €" + converter(amount,gbp_usd))


  #eur currencies
  if currencyFrom == "EUR" and currencyTo == "USD":
    print("You get: €" + converter(amount,eur_usd))

  if currencyFrom == "EUR" and currencyTo == "GBP":
    print("You get: €" + converter(amount,eur_gbp))


  #usd currencies
  if currencyFrom == "USD" and currencyTo == "GBP":
    print("You get: €" + converter(amount,usd_gbp))

  if currencyFrom == "USD" and currencyTo == "EUR":
    print("You get: €" + converter(amount,usd_eur))

  print("Would you like to convert another currency? ")
  choice = input()

  if choice == "Yes":
    print()
  else:
    break
