#FirstProgram.py
#Name: Carter Schmid
#Date: 8/28/2024
#Assignment: Lab 1

def main():
  print("First Program")
  #Say hello
  print("Hello")
  #Ask for the user's name
  name = input("What is your name? ")
  print(name)
  #Use the user's name in the program.

  #Ask the user for their age.
  age = input("What is your age? ")
  print(age)
  #Tell the user what year they were born in.
  age = int(age)
  birthYear = 2024 - age
  #Assume that they have not had their birthday yet this year.
  print("You were born in", birthYear)

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
