
#This will ask the client/user to Enter the time taken for swimming, cycling and running
swimmingTime = float(input("Enter the time taken for swimming (in minutes): "))
cyclingTime = float(input("Enter the time taken for cycling (in minutes): "))
runningTime = float(input("Enter the time taken for running (in minutes): "))



# This will calculate the overall time (swimming + cycling + running)
overallTime = swimmingTime + cyclingTime + runningTime


#This will determine the prizes depending on the overall time taken
if overallTime <= 100:
    print("Congratulations! You have earned Provincial colours.")
elif overallTime <= 105:
    print("Congratulations! You have earned Provincial half colours.")
elif overallTime <= 110:
    print("Congratulations! You have earned Provincial Scroll.")
else:
    print("Sorry, you did not qualify for an award.")