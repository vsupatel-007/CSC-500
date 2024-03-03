room_number = {"CSC101" : 3004, "CSC102" : 4501, "CSC103" : 6755, "NET110" : 1244, "COM241": 1411}
instructor = {"CSC101" : "Haynes", "CSC102" : "Alvarado", "CSC103" : "Rich", "NET110" : "Burke", "COM241": "Lee"}
meeting_time = {"CSC101" : "8:00 a.m.", "CSC102" : "9:00 a.m.", "CSC103" : "10:00 a.m.", "NET110" : "11:00 a.m.", "COM241": "1:00 p.m."}

course_input = str(input("Enter course number --> "))

print(" ----- " + course_input +" -----")
print("Room number:", room_number[course_input])
print("Instructor:", instructor[course_input])
print("Meeting time:", meeting_time[course_input])