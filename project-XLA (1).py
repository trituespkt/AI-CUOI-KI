from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from numpy import place
from tkinter import Canvas
import cv2
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from tensorflow.keras.utils import load_img, img_to_array
from tkinter import filedialog
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'D:\\ProjectAI\\tesseract.exe'
import numpy as np

    


def Form_Trinh_Bay():
    present = Tk()
    present.title("PROJECT:PHAT HIEN NHAC CU")
    present.geometry("1000x800")
     #đưa ra giữa màn hình
    present.update_idletasks()
    width = present.winfo_width()
    frm_width = present.winfo_rootx() - present.winfo_x()
    win_width = width + 2 * frm_width
    height = present.winfo_height()
    titlebar_height = present.winfo_rooty() - present.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = present.winfo_screenwidth() // 2 - win_width // 2
    y = present.winfo_screenheight() // 2 - win_height // 2
    present.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    #ve khung
    rec_cam = Canvas(present, bg= "white",height= 490, width= 490).place(x= 500, y= 300)
 

    return

def Form_Gioi_Thieu(): 
    #khởi tạo form
    window = Tk()
    window.title("GIỚI THIỆU ĐỀ TÀI ")
    window.geometry("1000x800") 
    #đưa ra giữa màn hình
    window.update_idletasks()
    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2 * frm_width
    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth() // 2 - win_width // 2
    y = window.winfo_screenheight() // 2 - win_height // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    #logo
    img_logo_ute = Image.open('logo.jpg')
    img_logo_ute = img_logo_ute.resize((150,150), Image.ANTIALIAS)
    img_logo_ute = ImageTk.PhotoImage(img_logo_ute)
    panel1 = Label(window, image= img_logo_ute).place(x= 20, y = 0)
    img_logo_khoa = Image.open('truong.jpg')
    img_logo_khoa = img_logo_khoa.resize((240,150), Image.ANTIALIAS)
    img_logo_khoa = ImageTk.PhotoImage(img_logo_khoa)
    panel2= Label(window, image= img_logo_khoa).place(x= 750, y = 0)
    #tên khoa + ngành
    lbl1 = tkinter.Label(window,text= "KHOA CƠ KHI CHẾ TẠO MÁY",fg="black",font= ("Arial",22,"bold")).place(x= 270, y= 10)
    lbl2 = tkinter.Label(window,text= "NGÀNH: KỸ THUẬT CÔNG NGHIỆP",fg="black",font= ("Arial",20,"bold")).place(x= 230, y= 45)
    lbl3 = tkinter.Label(window,text= "MÔN HỌC: TRÍ TUỆ NHÂN TẠO",fg="black",font= ("Arial",20,"bold")).place(x= 280, y= 80)
    
    #khởi tạo tên đề tài
    lbl5 = tkinter.Label(window,text= "Tên đề tài:",fg="red",font= ("Times",25,"italic")).place(x= 400, y= 140)
    lbl6 = tkinter.Label(window,text= "PHÁT HIỆN ",fg="red",font= ("Times",27)).place(x= 380, y= 190)
    lbl7 = tkinter.Label(window,text= "CÁC LOẠI NHẠC CỤ CỔ TRUYỀN VIỆT NAM",fg="red",font= ("times",27)).place(x= 80, y= 240)
    #vẽ khung thành viên
    rec = Canvas(window, bg= "darksalmon",height= 490, width= 490).place(x= 500, y= 300)
    #hình đề tài
    img_hand = Image.open('nền.jpg')
    img_hand = img_hand.resize((490,490), Image.ANTIALIAS)
    img_hand = ImageTk.PhotoImage(img_hand)
    panel3 = Label(window, image= img_hand)
    panel3.place(x=10,y=300)
    #Tên thành viên 
    lbl8 = tkinter.Label(window,text= "GVHD: PGS. TS. Nguyễn Trường Thịnh",fg="black",font= ("Arial",18,"italic","bold"),bg="darksalmon").place(x= 520, y= 305)
    lbl9 = tkinter.Label(window,text= "SVTH : Mai Thị Trí Tuệ",fg="black",font= ("Arial",20,"bold"),bg="darksalmon").place(x= 520, y= 370)
    lbl13 = tkinter.Label(window,text= "MSSV : 20104070",fg="black",font= ("Arial",20,"italic","bold"),bg="darksalmon").place(x= 520, y= 440)
  
    def open_image():
        filename = filedialog.askopenfilename()
        img = Image.open(filename)
        x =int(img.size[0])
        y =int(img.size[1])
        img2 =img.resize((x,y))
        imgtk= ImageTk.PhotoImage(img)
        panel3.config(image=imgtk, width= 500, height= 600)
        panel3.img=imgtk
        def nhandien():
            model = load_model('NhaccuVN.h5')
            img5 = load_img(filename,target_size=(150,150))
            plt.imshow(img5)
            img5=img_to_array(img5)
            img5=img5.astype('float32')
            img5=img5/255
            img5=np.expand_dims(img5,axis=0)
            result=model.predict(img5)
            class_nhaccu=['Cong chieng',
 'Dan Da',
 "Dan T'rung",
 'Dan Tam',
 'Dan Tranh',
 'Dan bau',
 'Dan gao',
 'Khen',
 'Sáo trúc',
 'dan sen',
 'Đàn Nhị',
 'Đàn nguyệt',
'Đàn tam thập lục',
 'Đàn tì bà'
 'Đàn Đáy']
            a= int(np.argmax(model.predict(img5),axis=1))
            print("Đây là nhạc cụ:", class_nhaccu[a])
            lable2= Label(text=class_nhaccu[a], bg="black",fg='white',font= 'arial 20').place(x=50,y=300)
        btn1= Button(window, text= "Nhận Diện",font=("Arial",18,"bold"),bg="white",fg= "red",command=nhandien).place(x=820, y= 600)

    
    
    
    #nút nhấn
 

    btn = Button(window, text= "Chọn ảnh",font=("Arial",18,"bold"),bg="white",fg= "red",command=open_image).place(x=550, y= 600)
    
    
    


    
    
    
    
    
    window.mainloop()
    return

Form_Gioi_Thieu()

