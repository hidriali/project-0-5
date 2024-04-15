#this program is named CraFinder for a company named AutoCountry.
#the program enables users to navigate through the menu options.

def CarFinder():

  print("AutoCountry")

 #recall the fuction  
CarFinder()

# display the list of cars 

AllowedVehiclesList= [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Rivian R1T', 'Ram 1500']


#start your loop 
while True:
   print()
   print("*******************************")

   print("AutoCountry Vehicle Finder v0.1")
   print("*******************************")
# declare/assign your variables choice-num1, choice-num2, choice-num3, choice_num4, choice_num5.
   choice_num1=("1. PRINT all Authorized Vehicles") 

   choice_num2=("2. SEARCH for Authorized Vehicle")

   choice_num3=("3. add authorized vehicle")

   choice_num4=("4. DELETE Authorized Vehicle")

   choice_num5=("5. Exit")


#allow the user to enter a number from 1 to 4 of the menue. 
   user_input=input("Please Enter the following number below from the following menu:" + choice_num1 + "\n" + choice_num2 + "\n" + choice_num3 + "\n" + choice_num4 + "\n" + choice_num5 + "\n")
  
  # start your if statement to direct the user to the correct path after the user chooses a number from the menu.

   if user_input == "1":
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
# this program will end the current iteration of the and start from the top of the loop, when the users input is 1.

# use *, sep= "\n" to print elements in new lines.
    print(*AllowedVehiclesList, sep= "\n")
  
    continue
  
   elif user_input=="5":
# this program will end after the user input 5. 
    
      print("Thank you for using the AutoCountry Vehicle Finder, good-bye! " )
      
      break



   
     

     

       

