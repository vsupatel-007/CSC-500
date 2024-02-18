#part2
book_number = int(input("Enter the number of book purchased this month--> "))
print(str(book_number), "books.")

if book_number == 0:
  print("You earned 0 points. Read more :(")

elif book_number > 0 and book_number <= 2:
  print("You earned 0 points. :|")

elif book_number > 2 and book_number <= 4:
  print("You earned 5 points. :|")

elif book_number > 4 and book_number <= 6:
  print("You earned 15 points. :|")

elif book_number > 6 and book_number <= 8:
  print("You earned 30 points. :|")

elif book_number > 8:
  print("You earned 60 points. :)")