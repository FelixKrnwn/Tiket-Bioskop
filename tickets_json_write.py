from json import dump

file_path = "newtxt/ticket.json"
mode = "w"

tickets = {
	"133029-F001A5" : {
		"customer" : "Felix",
		"judul" : "Anabelle",
		"jam" : "13 45",
		"tanggal" : "29 Oktober 2020",
		"studio" : "5",
		"kursi" : "F15"
	},
	"20301-A002S2" : {
		"customer" : "Dodo",
		"judul" : "Spriderman, Far From Home",
		"jam" : "20 45",
		"tanggal" : "1 November 2020",
		"studio" : "2",
		"kursi" : "A2"
	}
}

with open(file_path, mode) as file:
	dump(tickets, file)