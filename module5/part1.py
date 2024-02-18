#part1
years = int(input("Enter the number of years --> "))
print(str(years) + " years.")

MONTHS = 12
for i in range(1 , years+1):
  sum = 0

  print("\t\t Year", str(i))
  for j in range(1, 13):
    rain = float(input("Enter inches of rainfall for year " + str(i) + " month " + str(j) + " -->" ))
    sum += rain

  print()
  print("Number of months monitored =", str(MONTHS), "months" )
  print("It rained in total of", str(round(sum,2)), "inches", "for", str(MONTHS), "months.")
  print("The average rainfall per month is", str(round(sum/MONTHS, 2)), "inches")
  print()
  print()