
b =[]
def prime_checker(number):
  remainders = number
  for a in range(2, number+1):
    b.append(int(a))
  # print(b)
  position = number -2
  print(b[position])
  b.pop(position)
  for c in b:
      if number % c != 0 : 
        remainders -= 1
  if remainders == 2:
    print("prime")
  else:
    print("not prime")
print("Welcome to the Prime Checker")
choice = input("What number do you want to check?")
prime_checker(int(choice))






