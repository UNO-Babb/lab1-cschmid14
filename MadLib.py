#MadLib.py
#Name: Carter Schmid
#Date: 8/28/2024
#Assignment: MadLib

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Enter a noun: ")
  verb1 = input("Enter a verb: ")
  adjective1 = input("Enter an adjective: ")
  noun2 = input("Enter a noun: ")
  verb2 = input("Enter a verb: ")
  adjective2 = input("Enter an adjective: ")
  
  #Print the story with the user supplied words.

  print("I drive a " + noun1 + "to school " + verb1 + "While my friend drives a" )

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
