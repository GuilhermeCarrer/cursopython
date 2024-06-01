print("Welcome to the tip calculator!")
totalbill = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
peoplesplit = int(input("How many people to split the bill? "))
entirebill = (totalbill + tip)/peoplesplit
formatted_num = "{:.2f}".format(entirebill)
print("Each person should pay: ",formatted_num)