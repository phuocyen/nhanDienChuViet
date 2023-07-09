
import PIL #thư viện xử lý ảnh
from PIL import ImageTk, Image, ImageDraw
from tkinter import * #thư viện thiết kế giao diện
from PIL import Image,ImageTk
import numpy as np # thư viện tính toán
import cv2 #thư viện xử lý ảnh

width = 200 # chiều rộng
height = 200 # chiều cao
white = (255, 255, 255)
black = (0, 0, 0)

def RUN():
    # đọc ảnh train và nhan dạng
	img = cv2.imread('digits.png',0)
	imgNhanDang = cv2.imread('image_20.png',0)
    # cắt cảnh thàng từng ô nhỏ
	cells = [np.hsplit(row, 100) for row in np.vsplit(img, 50)]
    # chuyển thành ma trận 2 chiều
	x = np.array(cells) 
	x2 = np.array(imgNhanDang) 
    # tạo du liệu train và du liệu test(nhandang)
	train = x[:,:50].reshape(-1, 400).astype(np.float32)
	test = x2.reshape(-1, 400).astype(np.float32)
    # dán nahxn cho du liệu test
	k = np.arange(10) 
	train_labels = np.repeat(k, 250)[:, np.newaxis] 
    # Nhận dạng 
	knn = cv2.ml.KNearest_create()
	knn.train(train, 0, train_labels)
	kq1, kq2, kq3, kq4 = knn.findNearest(test, 20)
	box.insert(END,"Kết quả là: {}".format(int(kq2)))
	
def CLEAR():
	box.delete(1.0,END)
	global image1, draw;
	cv.delete("all")
	image1 = PIL.Image.new("RGB", (width, height), black)
	draw = ImageDraw.Draw(image1)

def SAVE():
	filename = "image.png"
	image1.save(filename)
	image = Image.open('image.png')
	new_image = image.resize((20, 20))
	new_image.save('image_20.png')

def paint(event):
    x1, y1 = (event.x - 3), (event.y - 3)
    x2, y2 = (event.x + 3 ), (event.y + 3)
    cv.create_line(x1, y1, x2, y2, fill="white",width=15)
    draw.line([x1, y1, x2, y2],fill="white",width=15)
	
root = Tk()
root.geometry("1280x721+90+30")
root.title("BÁO CÁO NHÓM")
background=Image.open("GIAODIEN.png")
render=ImageTk.PhotoImage(background)
img3=Label(root, image=render)
img3.place(x=0, y=0)

cv = Canvas(root, width=width, height=height, bg='black')
cv.place(x=100, y= 220)

image1 = PIL.Image.new("RGB", (width, height), black)
draw = ImageDraw.Draw(image1)


cv.bind("<B1-Motion>", paint)

button_frame=Frame(root).pack(side=BOTTOM)
save_button=Button(button_frame,text="Lưu",font=(("Times New Romen"),15,'bold'),command=SAVE)
# button2=Button(text="Clear",command=Clear)
save_button.place(x=170, y= 430)
# button2.pack(side = RIGHT)

box=Text(root, width=25, height=1, font=("Times New Romen",13))
box.pack(pady=300)

button_frame=Frame(root).pack(side=BOTTOM)
run_button=Button(button_frame,text="Chạy",font=(("Times New Romen"),15,'bold'),command=RUN)
run_button.place(x=545, y= 325)

button_frame=Frame(root).pack(side=BOTTOM)
clear_button=Button(button_frame,text="Xóa",font=(("Times New Romen"),15,'bold'),command=CLEAR)
clear_button.place(x=680, y= 325)
root.mainloop()




