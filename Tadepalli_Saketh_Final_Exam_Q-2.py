def main(): # defining a function called main.
	user_input1=""  #empty string assigned to variable.
	while user_input1!="N": #while loop is initiated until the user inputs "N".
		user_input1=int(input("\nEnter the positive number: ")) #Allows users to enter number. 
		print(f"All Factor of {user_input1} are displayed: ")
		arr = [] #an empty array set is declared .
		for x in range(1,user_input1+1): #for loop is initiated with x having range from 1 to user_input+1.
			if user_input1%x==0: # if the user input is divided with x the reminder should be equal to zero.
				print(x,end=",")
				arr.append(x) #adding x into empty array.
		if (len(arr)<10): #if length of array is less than 10.
			print("\nThis is too less.")
			print("\nDo you want to continue?")
			user_input2=input("Enter (Y/N): ")
			if user_input2=="Y": #if user presses "Y".
				main() #calling the function main created above.
			else:
				print("\nThank you") #else print "thank you".
			break #break statement is used to exit loop.
				
		if (len(arr)>10): #if length of array is greater than 10.
			last_element=arr[-3:] #getting the last 3 highest factors from array.
			print("\nThe highest 3 factors: ",last_element) 
			average= sum(last_element)/len(last_element) #calculating average by sum/len of last 3 factors from array.
			print("The Average of highest 3 factors: ",(round(average,3))) # rounding of decimals to 100th position.
			print("\nDo you want to continue?")
			user_input2=input("Enter (Y/N): ")
			if user_input2=="Y": #if user presses "Y".
				main() #calling the function main created above.
			else:
				print("\nThank you") #else print "thank you".
			break	#break statement is used to exit loop.		 
main() #calling the function to perform.
				

				
			
