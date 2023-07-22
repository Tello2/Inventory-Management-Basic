from typing import List

def menu():
	print("\t\t\t\t\t\tMENU QUẢN LÝ KHO HÀNG")
	print("*------------------------------------------------------------------------------------------------------------*")
	print("\t\t*0.  Thoát chương trình.                                                *")
	print("\t\t*1.  Nhập dữ liệu từ FILE có sẵn.                                       *")
	print("\t\t*2.  Nhập dữ liệu từ bàn phím.                                          *")
	print("\t\t*3.  Thêm phần tử ở vị trí tự chọn trong danh sách.                     *")
	print("\t\t*4.  Xóa phần tử ở vị trí tự chọn trong danh sách.                      *")
	print("\t\t*5.  Sắp xếp danh sách theo tải trọng.                                  *")
	print("\t\t*6.  Thêm 1 kho vào danh sách và đảm bảo thứ tự sắp xếp ở câu 5.        *")
	print("\t\t*7.  Tìm danh sách các kho nào vừa được nhập hàng vào tháng 10 năm 2021.*")
	print("\t\t*8.  Tìm kho nào còn trống (tức tải trọng hàng đã nhập < tải trọng).    *")
	print("\t\t*9.  Tìm xem kho nào có thể chứa loại hàng hoá là \"hàng đông lạnh\".     *")
	print("\t\t*10. Tìm tải trọng trung bình của toàn bộ những kho hàng nào ở Đồng Nai.*")
	print("\t\t*11. Có bao nhiêu kho hàng có tên bắt đầu bằng \"KH\".                    *")
	print("\t\t*12. Xuất danh sách kho.                                                *")
	print("*------------------------------------------------------------------------------------------------------------*")

def menuCau3_4(s):
	print("\n0.  Không thực hiện.")
	print("1.  " + s +" Vị trí đầu.")
	print("2.  " + s +" Vị trí bất kỳ.")
	print("3.  " + s +" Vị trí cuối.")

class KhoHang:
	def __init__(
		self, ma, ten, diadiem, taitrong, loai, ngaynhap, ngayxuat, taitrongnhap
	):
		self.ma = ma
		self.ten = ten
		self.dia_diem = diadiem
		self.tai_trong = taitrong
		self.loai = loai
		self.ngay_nhap = ngaynhap
		self.ngay_xuat = ngayxuat
		self.tai_trong_nhap = taitrongnhap

	def __str__(self):
		return f"\t{self.ma}\t\t{self.ten}\t{self.dia_diem}\t{self.tai_trong}\t\t{self.loai}\t\t{self.ngay_nhap}\t\t{self.ngay_xuat}\t\t{self.tai_trong_nhap}"


class Node(object):
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def __show__(self):
		node = self.head
		countTT = 0
		print("\nSTT\tMã kho hàng\tTên kho hàng\tĐịa điểm\tTải trọng\tLoại hàng hóa\t\tNgày nhập kho\t\tNgày xuất kho\t\tTải trọng nhập\n")
		while node is not None:
			print(countTT, node.data)
			node = node.next
			countTT += 1
	def __size__(self):
		node = self.head
		count = 0
		while node is not None:
			count += 1
			node = node.next
		return count
	def __delete__(self,pos): # 0 là vị trí đầu tiên  , size - 1 là vị trí cuối cùng
		if self.head is None or pos < 0 or pos > self.__size__() - 1:
			return
		if pos == 0:
			self.head = self.head.next
			return
		if pos == self.__size__() - 1:
			node = self.head
			while node.next != self.tail:
				node = node.next
			node.next = None
			self.tail = node
			return
		prev = self.head
		count = 0
		while prev is not None:
			if count == pos-1:
				break
			count += 1
			prev = prev.next
		prev.next = prev.next.next
	def AddHead(self,data):
		node = Node(data)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			node.next = self.head
			self.head = node
	
	def addPhanTu(self,data,pos):
		if pos < 0:
			pos = 0
		if pos > self.__size__():
			pos = self.__size__()
		node = Node(data)
		if (self.head is None) | (pos == 0):
			self.AddHead(data)
			return
		i = 0
		p = self.head
		while i != pos - 1:
			i += 1
			p = p.next
		node.next = p.next
		p.next = node
		if node.next == None:
			self.tail = node

	def __sort__(self):
		if self.head is None:
			return
		node = self.head
		while node.next is not None:
			next_node = node.next
			while next_node is not None:
				if int(node.data.tai_trong) > int(next_node.data.tai_trong):
					node.data, next_node.data = next_node.data, node.data
				next_node = next_node.next
			node = node.next
	def __countKhoHangBatDauBangKH__(self):
		node = self.head
		count = 0 
		while node is not None:
			if "KH" in node.data.ma[:2]:
				count += 1
			node = node.next
		return count
	def __inDSKhoNhapVaoThang10Nam2021__(self):
		node = self.head
		count = 0
		countTT = 0
		while node is not None:
			if "10/2021" in node.data.ngay_nhap:
				count +=1
				if count == 1:
					print("Danh sách kho có hàng nhập vào tháng 10 năm 2021:")
					print("\nSTT\tMã kho hàng\tTên kho hàng\tĐịa điểm\tTải trọng\tLoại hàng hóa\t\tNgày nhập kho\t\tNgày xuất kho\t\tTải trọng nhập")
				print(countTT,node.data)
			countTT += 1
			node = node.next
		if count == 0:
			print("Không tồn tại kho nhập vào tháng 10 năm 2021.")
	def __inDSKhoConTrong__(self):
		node = self.head
		count = 0
		countTT = 0
		while node is not None:
			if int(node.data.tai_trong_nhap) < int(node.data.tai_trong):
				count +=1
				if count == 1:
					print("Danh sách các kho còn trống:")
					print("\nSTT\tMã kho hàng\tTên kho hàng\tĐịa điểm\tTải trọng\tLoại hàng hóa\t\tNgày nhập kho\t\tNgày xuất kho\t\tTải trọng nhập")
				print(countTT, node.data)
			countTT += 1
			node = node.next
		if count == 0:
			print("Không còn kho nào trống cả.")
	def __inDSKhoChuaHangDongLanh__(self):
		node = self.head
		count = 0
		countTT = 0
		while node is not None:
			if ("dong lanh" in node.data.loai) | ("đông lạnh" in node.data.loai):
				count += 1
				if count == 1:
					print("Danh sách các kho chứa hàng đông lạnh.")
					print("\nSTT\tMã kho hàng\tTên kho hàng\tĐịa điểm\tTải trọng\tLoại hàng hóa\t\tNgày nhập kho\t\tNgày xuất kho\t\tTải trọng nhập")
				print(countTT, node.data)
			countTT += 1
			node = node.next
		if count == 0:
			print("Không có kho nào chứa được hàng đông lạnh.")
	def __averageTaiTrongKhoDongNai__(self):
		node = self.head
		sumDN = 0
		countDN = 0
		while node is not None:
			if ("Dong Nai" in node.data.dia_diem) | ("Đồng Nai" in node.data.dia_diem):
				sumDN += float(node.data.tai_trong)
				countDN += 1
			node = node.next
		if countDN == 0:
			return 0
		return float(sumDN) / countDN
	def __addPTTheoTaiSapXepTaiTrong__(self, data):
		if self.head is None:
			self.AddHead(data)
			return
		node = Node(data)
		p = self.head
		if self.head == self.tail:
			if p.data.tai_trong > node.data.tai_trong:
				self.AddHead(data)
				return
			else:
				p.next = node
				self.tail = node
				return
		else:
			i = 0
			while p.data.tai_trong < node.data.tai_trong:
				i += 1
				p = p.next
				if p == self.tail:
					self.addPhanTu(data,self.__size__())
					return
			self.addPhanTu(data, i)


def ReadFile(ListKhoHang):
	try:
		f = open("KhoHang.txt", "r")
		for line in f:
			line = line.strip()
			line = line.split(",")
			ListKhoHang.append(
				KhoHang(
					line[0],
					line[1],
					line[2],
					line[3],
					line[4],
					line[5],
					line[6],
					line[7],
				)
			)
		print("Đọc FILE thành công.")
		f.close()
	except:
		print("Loi doc file")


def NhapDs(LinkedList):
	n = int(input("Nhập số lượng kho hàng: "))
	for i in range(n):
		print("\nNhập dữ liệu kho hàng thứ " + str(i) + ":")
		check = 0
		while check == 0:
			check = 1
			ma = input("Nhập mã kho hàng (không trùng mã kho hàng khác): ")
			node = LinkedList.head
			while node is not None:
				if node.data.ma == ma:
					check = 0
					break
				node = node.next
		ten = input("Nhập tên kho hàng: ")
		diadiem = input("Nhập địa điểm: ")
		taitrong = input("Nhập tải trọng: ")
		loai = input("Nhập loại: ")
		ngaynhap = input("Nhập ngày nhập: ")
		ngayxuat = input("Nhập ngày xuất: ")
		taitrongnhap = input("Nhập tải trọng nhập: ")
		LinkedList.append(
			KhoHang(ma, ten, diadiem, taitrong, loai, ngaynhap, ngayxuat, taitrongnhap)
		)
def Nhap1Kho(LinkedList, pos):
	check = 0
	while check == 0:
		check = 1
		ma = input("Nhập mã kho hàng (không trùng mã kho hàng khác): ")
		node = LinkedList.head
		while node is not None:
			if node.data.ma == ma:
				check = 0
				break
			node = node.next
	ten = input("Nhập tên kho hàng: ")
	diadiem = input("Nhập địa điểm: ")
	taitrong = input("Nhập tải trọng: ")
	loai = input("Nhập loại: ")
	ngaynhap = input("Nhập ngày nhập: ")
	ngayxuat = input("Nhập ngày xuất: ")
	taitrongnhap = input("Nhập tải trọng nhập: ")
	LinkedList.addPhanTu(KhoHang(ma, ten, diadiem, taitrong, loai, ngaynhap, ngayxuat, taitrongnhap), pos)
def Nhap1KhoSXTheoTaiTrong(LinkedList):
	check = 0
	while check == 0:
		check = 1
		ma = input("Nhập mã kho hàng (không trùng mã kho hàng khác): ")
		node = LinkedList.head
		while node is not None:
			if node.data.ma == ma:
				check = 0
				break
			node = node.next
	ten = input("Nhập tên kho hàng: ")
	diadiem = input("Nhập địa điểm: ")
	taitrong = input("Nhập tải trọng: ")
	loai = input("Nhập loại: ")
	ngaynhap = input("Nhập ngày nhập: ")
	ngayxuat = input("Nhập ngày xuất: ")
	taitrongnhap = input("Nhập tải trọng nhập: ")
	LinkedList.__addPTTheoTaiSapXepTaiTrong__(KhoHang(ma, ten, diadiem, taitrong, loai, ngaynhap, ngayxuat, taitrongnhap))


def main():
	ListKhoHang = LinkedList()
	data = None
	checksort = 0
	while 1:
		menu()
		chon=int(input("Nhập lựa chọn: "))
		if chon == 1:
			ReadFile(ListKhoHang)
		elif chon == 2:
			NhapDs(ListKhoHang)
		elif chon == 3:
			menuCau3_4("Thêm")
			chonCau4=int(input("Nhập lựa chọn câu 3: "))
			if chonCau4 == 1:
				Nhap1Kho(ListKhoHang, 0)
				print("Đã thêm phần tử vào vị trí đầu tiên.")
				checksort = 0
			elif chonCau4 == 2:
				viTriThem=int(input("Nhập vị trí thêm: "))
				Nhap1Kho(ListKhoHang, viTriThem)
				print("Đã thêm phần tử ở vị trí thứ " + str(viTriThem))
				checksort = 0
			elif chonCau4 == 3:
				Nhap1Kho(ListKhoHang, ListKhoHang.__size__())
				print("Đã thêm phần tử vào vị trí cuối.")
				checksort = 0
			elif chonCau4 == 0:
				print("Không thực hiện gì hết.")
			else:
				print("Không tìm thấy yêu cầu khác.")
		elif chon == 4:
			ListKhoHang.__show__()
			menuCau3_4("Xóa")
			chonCau4=int(input("Nhập lựa chọn câu 4: "))
			if chonCau4 == 1:
				ListKhoHang.__delete__(0)
				print("Đã xóa phần tử đầu tiên.")
			elif chonCau4 == 2:
				viTriXoa=int(input("Nhập vị trí xóa: "))
				ListKhoHang.__delete__(viTriXoa)
				print("Đã xoá phần tử thứ " + str(viTriXoa))
			elif chonCau4 == 3:
				ListKhoHang.__delete__(ListKhoHang.__size__() -1)
				print("Đã xóa phần tử cuối.")
			elif chonCau4 == 0:
				print("Không thực hiện gì hết.")
			else:
				print("Không tìm thấy yêu cầu khác.")
		elif chon == 5:
			ListKhoHang.__sort__()
			print("Đã sắp xếp theo tải trọng.")
			checksort = 1
		elif chon == 6:
			if checksort == 0:
				ListKhoHang.__sort__()
				checksort = 1
			Nhap1KhoSXTheoTaiTrong(ListKhoHang)
		elif chon == 7:
			ListKhoHang.__inDSKhoNhapVaoThang10Nam2021__()
		elif chon == 8:
			ListKhoHang.__inDSKhoConTrong__()
		elif chon == 9:
			ListKhoHang.__inDSKhoChuaHangDongLanh__()
		elif chon == 10:
			print("Trung bình tải trọng của những kho hàng ở Đồng Nai là: " + str(ListKhoHang.__averageTaiTrongKhoDongNai__()))
		elif chon == 11:
			print("\nKho gồm có " + str(ListKhoHang.__countKhoHangBatDauBangKH__()) + " kho hàng có tên bắt đầu bằng \"KH\"")
		elif chon == 12:
			ListKhoHang.__show__()
		elif chon==0:
			print("Thoát chương trình.")
			break;
		else:
			print("Không tìm thấy yêu cầu khác.")



if __name__ == "__main__":
	main()
