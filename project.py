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

def print_data(id_pesanan=None, customer=True, judul=True, jam=True, tanggal=True, studio=True, kursi=True,all_data=False):
	if id_pesanan != None and all_data == False:
		print(f"NOMOR TIKET : {id_pesanan}")
		print(f"NAMA CUSTOMER : {tickets[id_pesanan]['customer']}")
		print(f"JUDUL : {tickets[id_pesanan]['judul']}")
		print(f"JAM : {tickets[id_pesanan]['jam']}")
		print(f"TANGGAL : {tickets[id_pesanan]['tanggal']}")
		print(f"STUDIO : {tickets[id_pesanan]['studio']}")
		print(f"KURSI : {tickets[id_pesanan]['kursi']}")
	elif kursi == False and all_data == False:
		print(f"NOMOR TIKET : {id_pesanan}")
		print(f"NAMA CUSTOMER : {tickets[id_pesanan]['customer']}")
		print(f"JUDUL : {tickets[id_pesanan]['judul']}")
		print(f"JAM : {tickets[id_pesanan]['jam']}")
		print(f"TANGGAL : {tickets[id_pesanan]['tanggal']}")
		print(f"STUDIO : {tickets[id_pesanan]['studio']}")
	elif all_data == True:
		for id_pesanan in tickets:
			customer = tickets[id_pesanan]["customer"]
			judul = tickets[id_pesanan]["judul"]
			jam = tickets[id_pesanan]["jam"]
			tanggal = tickets[id_pesanan]["tanggal"]
			studio = tickets[id_pesanan]["studio"]
			kursi = tickets[id_pesanan]["kursi"]
			print(f"NOMOR PESANAN : {id_pesanan} - NAMA CUSTOMER : {customer} - JUDUL : {judul} - JAM : {jam} - TANGGAL : {tanggal} - STUDIO : {studio} - NOMOR KURSI : {kursi}")

def view_tickets():
	print_header("DAFTAR TIKET TERSIMPAN")
	if not_empty(tickets):
		print_data(all_data=True)
	else:
		print("MAAF BELUM ADA TIKET TERSIMPAN")
	input("Tekan ENTER untuk kembali ke MENU")

def create_id_pesanan(customer, judul, jam, tanggal, studio, kursi):
	nama = customer[0]
	hari = datetime.now()
	jam = hari.hour
	tanggal = hari.day
	cinema = studio

	counter = len(tickets) + 1
	first = judul[0].upper()
	last_1 = kursi[0]
	
	id_pesanan = ("%s%04d%02d-%s%03d%s%s" % (nama, jam, tanggal, last_1, counter, first, cinema))
	return id_pesanan


def add_ticket():
	print_header("MENAMBAHKAN TIKET BARU")
	customer = input("NAMA CUSTOMER \t: ")
	judul = input("JUDUL \t: ")
	jam = input("JAM \t: ")
	tanggal = input("TANGGAL \t: ")
	studio = input("STUDIO \t: ")
	kursi = input("NOMOR KURSI \t: ")
	respon = input(f"Apakah yakin ingin membuat tiket : {customer} ? (Y/N) ")
	if verify_ans(respon):
		id_pesanan = create_id_pesanan(customer=customer, judul=judul, jam=jam, tanggal=tanggal, studio=studio, kursi=kursi)
		tickets[id_pesanan] = {
			"customer" : customer,
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

def searching_by_name(ticket):
	for id_pesanan in tickets:
		if tickets[id_pesanan]['customer'] == ticket:
			return id_pesanan
	else:
		return False


def find_ticket():
	print_header("MENCARI TIKET")
	customer = input(" Nama Customer tiket yang Dicari : ")
	exists = searching_by_name(customer)
	if exists:
		print("Tiket Ditemukan")
		print_data(id_pesanan=exists)
	else:
		print("Tiket Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def delete_ticket():
	print_header("MENGHAPUS TIKET")
	customer = input(" Nama Customer yang akan Dihapus : ")
	exists = searching_by_name(customer)
	if exists:
		print_data(id_pesanan=exists)
		respon = input(f"Yakin ingin menghapus {customer} ? (Y/N) ")
		if verify_ans(respon):
			del tickets[exists]
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

def update_ticket_customer(id_pesanan):
	print(f"Nama Lama : {tickets[id_pesanan]['customer']}")
	new_name = input("Masukkan Nama baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tickets[id_pesanan]['customer'] = new_name
		print("Data Telah di simpan")
		print_data(id_pesanan)
	else:
		print("Data Batal diubah")

def update_ticket_judul(id_pesanan):
	print(f"Judul Lama : {tickets[id_pesanan]['judul']}")
	new_title = input("Masukkan Judul baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tickets[id_pesanan]['judul'] = new_title
		print("Data Telah di simpan")
		print_data(id_pesanan)
	else:
		print("Data Batal diubah")

def update_ticket_jam(id_pesanan):
	print(f"Jam nonton Lama : {tickets[id_pesanan]['jam']}")
	new_hour = input("Masukkan Jam nonton baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tickets[id_pesanan]['jam'] = new_hour
		print("Data Telah di simpan")
		print_data(id_pesanan)
	else:
		print("Data Batal diubah")

def update_ticket_tanggal(id_pesanan):
	print(f"Tanggal Lama : {tickets[id_pesanan]['tanggal']}")
	new_date = input("Masukkan Tanggal baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tickets[id_pesanan]['tanggal'] = new_date
		print("Data Telah di simpan")
		print_data(id_pesanan)
	else:
		print("Data Batal diubah")

def update_ticket_studio(id_pesanan):
	print(f"Studio Lama : {tickets[id_pesanan]['studio']}")
	new_studio = input("Masukkan Studio baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tickets[id_pesanan]['studio'] = new_studio
		print("Data Telah di simpan")
		print_data(id_pesanan)
	else:
		print("Data Batal diubah")

def update_ticket_nomor(id_pesanan):
	print(f"Nomor Kursi Lama : {tickets[id_pesanan]['kursi']}")
	new_chair = input("Masukkan Nomor Kursi baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tickets[id_pesanan]['kursi'] = new_chair
		print("Data Telah di simpan")
		print_data(id_pesanan)
	else:
		print("Data Batal diubah")

def update_ticket():
	print_header("MENGUPDATE INFO TIKET")
	customer = input("Nama Customer yang akan di-update : ")
	exists = searching_by_name(customer)
	if exists:
		print_data(exists)
		print("EDIT FIELD [1] NAMA CUSTOMER [2] JUDUL - [3] JAM - [4] TANGGAL - [5] STUDIO - [6] NOMOR KURSI")
		respon = input("MASUKAN PILIHAN (1/2/3/4/5) : ")
		if respon == "1":
			update_ticket_customer(exists)
		if respon == "2":
			update_ticket_judul(exists)
		elif respon == "3":
			update_ticket_jam(exists)
		elif respon == "4":
			update_ticket_tanggal(exists)
		elif respon == "5":
			update_ticket_studio(exists)
		elif respon == "6":
			update_ticket_nomor(exists)
		saved = save_data_tickets()
		if saved:
			print("Data Tiket Telah di-update.")
		else:
			print("Kesalahan saat mengupdate")

	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def about_application():
	system("cls")
	print_header("TENTANG APLIKASI")
	print("""APLIKASI TIKETING BIOSKOP SEDERHANA
		DIBUAT OLEH : Felix Kurniawan
		TANGGAL PEMBUATAN : 19 November 2020
		""")
	return True


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
		return True
		while True:
			input("Tekan ENTER untuk kembali ke MENU")

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
file_path = "newtxt/tickets.json"
tickets = load_data_tickets()
while not stop:
	print_menu()
	user_input = input("Pilihan : ")
	stop = check_user_input(user_input)

