from json import load

file_path = "filetxt/tickets.json"
mode = "r"

with open(file_path, mode) as file:
	tickets = load(file)

clean_names = []

for ticket in tickets:
	clean_names.append(ticket.strip())
print(clean_names)
