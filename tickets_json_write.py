from json import dump

file_path = "filetxt/tickets.json"
mode = "w"

tickets = {
	"133029-F001A5" : {
		"judul" : "Anabelle\n",
		"jam" : "13 45\n",
		"tanggal" : "29 Oktober 2020\n",
		"studio" : "5\n",
		"kursi" : "F15\n"
	},
	"20301-A002S2" : {
		"judul" : "Spriderman, Far From Home",
		"jam" : "20 45",
		"tanggal" : "1 November 2020",
		"studio" : "2",
		"kursi" : "A2"
	}
}

with open(file_path, mode) as file:
	dump(tickets, file)