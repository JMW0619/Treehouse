attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben J.", "Dave"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "potential_attendess currently")

to_line = ", ".join(attendees) #converts list to string (Line 3)
cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("CC: " + cc_line)

to_line.split(", ") #converts string back to list (Line 8)
