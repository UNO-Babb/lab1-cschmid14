#MadLib.py
#Name: Carter Schmid
#Date: 8/28/2024
#Assignment: MadLib

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Enter a noun: ")
  adverb1 = input("Enter an adverb: ")
  noun2 = input("Enter a noun: ")
  noun3 = input("Enter a noun: ")
  adverb2 = input("Enter an adverb: ")
  adjective1 = input("Enter an adjective: ")
  
  #Print the story with the user supplied words.

  print("I drive a " + noun1 + " to school " + adverb1 + " With my " + noun2 + " in the back seat." )
  print("While my friend rides their " + noun3 + " to work " + adverb2 + " while holding a " + adjective1 + " backpack." )

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
