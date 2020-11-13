from os import system
from json import dump, load
from datetime import datetime

def print_menu():
	system("cls")
	print("""
	Aplikasi Tiket Bioskop Sederhana
	[1]. Lihat Semua Tiket
	[2]. Tambah Tiket Baru
	[3]. Cari Tiket
	[4]. Hapus Tiket
	[5]. Update Tiket
	[6]. Tentang Aplikasi
	[Q]. Keluar
		""")

def print_header(msg):
	system("cls")
	print(msg)

def not_empty(container):
	if len(container) != 0:
		return True
	else:
		return False

def verify_ans(char):
	if char.upper() == "Y":
		return True
	else:
		return False

def print_data(id_pesanan=None, judul=True, jam=True, tanggal=True, studio=True, kursi=True,all_data=False):
	if id_pesanan != None and all_data == False:
		print(f"NOMOR TIKET : {id_pesanan}")
		print(f"JUDUL : {tickets[id_pesanan]['judul']}")
		print(f"JAM : {tickets[id_pesanan]['jam']}")
		print(f"TANGGAL : {tickets[id_pesanan]['tanggal']}")
		print(f"STUDIO : {tickets[id_pesanan]['studio']}")
		print(f"KURSI : {tickets[id_pesanan]['kursi']}")
	elif kursi == False and all_data == False:
		print(f"NOMOR TIKET : {id_pesanan}")
		print(f"JUDUL : {tickets[id_pesanan]['judul']}")
		print(f"JAM : {tickets[id_pesanan]['jam']}")
		print(f"TANGGAL : {tickets[id_pesanan]['tanggal']}")
		print(f"STUDIO : {tickets[id_pesanan]['studio']}")
		print(f"KURSI : {tickets[id_pesanan]['kursi']}")
	elif all_data == True:
		for id_pesanan in tickets:
			judul = tickets[id_pesanan]["judul"]
			jam = tickets[id_pesanan]["jam"]
			tanggal = tickets[id_pesanan]["tanggal"]
			studio = tickets[id_pesanan]["studio"]
			kursi = tickets[id_pesanan]["kursi"]
			print(f"NOMOR PESANAN : {id_pesanan} - JUDUL : {judul} - JAM : {jam} - TANGGAL : {tanggal} - STUDIO : {studio} - NOMOR KURSI : {kursi}")

def view_tickets():
	print_header("DAFTAR TIKET TERSIMPAN")
	if not_empty(tickets):
		print_data(all_data=True)
	else:
		print("MAAF BELUM ADA TIKET TERSIMPAN")
	input("Tekan ENTER untuk kembali ke MENU")

def create_id_pesanan(judul, jam, tanggal, studio, kursi):
	hari = datetime.now()
	jam = hari.hour
	tanggal = hari.day
	cinema = studio

	counter = len(tickets) + 1
	first = judul[0].upper()
	last_1 = kursi[0]
	
	id_pesanan = ("%04d%02d-%s%03d%s%s" % (jam, tanggal, last_1, counter, first, cinema))
	return id_pesanan


def add_ticket():
	print_header("MENAMBAHKAN TIKET BARU")
	judul = input("JUDUL \t: ")
	jam = input("JAM \t: ")
	tanggal = input("TANGGAL \t: ")
	studio = input("STUDIO \t: ")
	kursi = input("NOMOR KURSI \t: ")
	respon = input(f"Apakah yakin ingin membuat tiket : {judul} ? (Y/N) ")
	if verify_ans(respon):
		id_pesanan = create_id_pesanan(judul=judul, jam=jam, tanggal=tanggal, studio=studio, kursi=kursi)
		tickets[id_pesanan] = {
			"judul" : judul,
			"jam" : jam,
			"tanggal" : tanggal,
			"studio" : studio,
			"kursi" : kursi
		}
		saved = save_data_tickets()
		if saved:
			print("Tiket telah dibuat.")
		else:
			print("Kesalahan saat membuat")
	else:
		print("TIKET Batal Dibuat")
	input("Tekan ENTER untuk kembali ke MENU")

def searching_by_id(ticket):
	if ticket in tickets:
		print('id_pesanan')

def find_ticket():
	print_header("MENCARI TIKET")
	nopes = input(" Nomor tiket yang Dicari : ")
	exists = searching_by_id(nopes)
	if exists:
		print("Tiket Ditemukan")
		print_data(id_pesanan=exists)
	else:
		print("Tiket Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def delete_ticket():
	print_header("MENGHAPUS TIKET")
	nopes = input(" Nomor tiket yang akan Dihapus : ")
	exists = searching_by_id(nopes)
	if exists:
		print_data(contact=exists)
		respon = input(f"Yakin ingin menghapus {id_pesanan} ? (Y/N) ")
		if verify_ans(respon):
			del tickets[id_pesanan]
			saved = save_data_tickets()
			if saved:
				print("Tiket Telah Dihapus")
			else:
				print("Kesalahan saat menghapus")
		else:
			print("Tiket Batal Dihapus")
	else:
		print("Tiket Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def update_ticket_judul(ticket):
	print(f"Judul Lama : {ticket}")
	new_title = input("Masukkan Judul baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tickets[new_title] = tickets[ticket]
		del tickets[ticket]
		print("Data Telah di simpan")
		print_data(new_title)
	else:
		print("Data Batal diubah")

def update_ticket_jam(ticket):
	print(f"Jam nonton Lama : {ticket}")
	new_hour = input("Masukkan Jam nonton baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tickets[new_hour] = tickets[ticket]
		del tickets[ticket]
		print("Data Telah di simpan")
		print_data(new_hour)
	else:
		print("Data Batal diubah")

def update_ticket_tanggal(contact):
	print(f"Tanggal Lama : {ticket}")
	new_date = input("Masukkan Tanggal baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tickets[new_date] = tickets[ticket]
		del tickets[ticket]
		print("Data Telah di simpan")
		print_data(new_date)
	else:
		print("Data Batal diubah")

def update_ticket_studio(contact):
	print(f"Studio Lama : {ticket}")
	new_studio = input("Masukkan Studio baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tickets[new_studio] = tickets[ticket]
		del tickets[ticket]
		print("Data Telah di simpan")
		print_data(new_studio)
	else:
		print("Data Batal diubah")

def update_ticket_nomor(contact):
	print(f"Nomor Kursi Lama : {ticket}")
	new_chair = input("Masukkan Nomor Kursi baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tickets[new_chair] = tickets[ticket]
		del tickets[ticket]
		print("Data Telah di simpan")
		print_data(new_chair)
	else:
		print("Data Batal diubah")

def update_ticket():
	print_header("MENGUPDATE INFO TIKET")
	nopes = input("Nomor Tiket yang akan di-update : ")
	exists = searching_by_id(nopes)
	if exists:
		print_data(id_pesanan)
		print("EDIT FIELD [1] JUDUL - [2] JAM - [3] TANGGAL - [4] STUDIO - [5] NOMOR KURSI")
		respon = input("MASUKAN PILIHAN (1/2/3) : ")
		if respon == "1":
			update_ticket_judul(nopes)
		elif respon == "2":
			update_ticket_jam(nopes)
		elif respon == "3":
			update_ticket_tanggal(nopes)
		elif respon == "4":
			update_ticket_studio(nopes)
		elif respon == "5":
			update_ticket_nomor(nopes)
		saved = save_data_tickets()
		if saved:
			print("Data Tiket Telah di-update.")
		else:
			print("Kesalahan saat mengupdate")

	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def about_application():
	print_header("TENTANG APLIKASI")
	print('''APLIKASI TIKETING BIOSKOP SEDERHANA
		DIBUAT OLEH : Felix Kurniawan
		TANGGAL PEMBUATAN : 28 Oktober 2020
		DISELESAIKAN PADA : 1 November 2020
		''')


def check_user_input(char):
	char = char.upper()
	if char == "Q":
		print("BYE!!!")
		return True
	elif char == "1":
		view_tickets()
	elif char == "2":
		add_ticket()
	elif char == "3":
		find_ticket()
	elif char == "4":
		delete_ticket()
	elif char == "5":
		update_ticket()
	elif char == "6":
		about_application()

def load_data_tickets():
	with open(file_path, 'r') as file:
		data = load(file)
	return data

def save_data_tickets():
	with open(file_path, 'w') as file:
		dump(tickets, file)
	return True


#flag/sign/tanda menyimpan sebuah kondisi
stop = False
file_path = "filetxt/tickets.json"
tickets = load_data_tickets()
while not stop:
	print_menu()
	user_input = input("Pilihan : ")
	stop = check_user_input(user_input)

