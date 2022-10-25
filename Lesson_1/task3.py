Numberofseconds = int(input("Enter number of seconds: "))
Seconds = Numberofseconds % 60
Minutes = ((Numberofseconds - Seconds)/60) % 60
Hours = (((Numberofseconds - Seconds)/60 - Minutes)/60) % 60
Days = (((((Numberofseconds - Seconds)/60 - Minutes)/60) - ((((Numberofseconds - Seconds)/60 - Minutes)/60) % 24))/24) % 24
print ("Days: " + str(Days), "Hours: " + str(Hours), "Minutes: " + str(Minutes), "Seconds: " + str(Seconds))