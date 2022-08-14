from distutils import command
from tkinter import*            #tkinter used to make powerfull gui application
from tkinter import ttk         # used to make stylish entry field.
from PIL import Image,ImageTk   #pip install pillow
import random,os                
from tkinter import messagebox
import tempfile
#from time import strftime
import sqlite3



class Bill_App:                              #first create a class then define a constructor ....
    def __init__(self,root):    #defining constructor using init funct;   WINDOW NAME =root
        self.root=root        #initailising root
        self.root.geometry("1530x800+0+0")    #windows width,size
        self.root.title("GROCERY BILL MANAGEMENT SYSTEM")

        # *************VARIABLES*****************
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        #self.product=StringVar()
        self.subcategory=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


        #Product categories list
        self.Category=["Select Option","Fruits","Vegetables","Dairy","Bread/Bakery","Cereals/Pulses","Snacks","Beverages"]
        self.SubCatFruits=["Apples","Mangoes","Bananas","Oranges","Watermelon"]
        self.price_Apples= 100
        self.price_Mangoes= 110
        self.price_banana=40
        self.price_Orange= 50
        self.price_watermelon= 70

        self.SubCatVeggie=["Potato","Tomato","Green chillies","Onion"]
        self.price_potato=40
        self.price_tomato=30
        self.price_green=15
        self.price_onion=50
        
        self.SubCatDairy=["Milk","Cheese","Egg","Paneer"]
        self.price_Milk= 40
        self.price_cheese = 110
        self.price_egg= 60
        self.price_paneer = 120

        self.SubCatBread=["Garlic bread","Brown bread","Multi grain","French bread"]
        self.price_garlic=40
        self.price_brown=45
        self.price_multi=50
        self.price_french=70

        self.SubCatCereals=["Rice","Wheat","Oats","Beans","Dry peas"]
        self.price_rice=45
        self.price_wheat=50
        self.price_oats=50
        self.price_beans=35
        self.price_drypeas=40
        
        self.SubCatSnacks=["Lays","Popcorn","Chocolates","Nachos"]
        self.price_lays=20
        self.price_popcorn=25
        self.price_Chocolates=30
        self.price_nachos=35
           
        self.SubCatBev=["Pepsi","Fruit juice","Cold Coffee"]
        self.price_pepsi=35
        self.price_fruitjuice=30
        self.price_Coldcoffee=40
        
        #image1             inserting images.
        img=Image.open("image/bread.jpg")
        img=img.resize((300,170),Image.ANTIALIAS)      #ANTIALIAS FUNCT converts high level image to low level.
        self.photoimg=ImageTk.PhotoImage(img)

        lb1_img=Label(self.root,image=self.photoimg)   #
        lb1_img.place(x=0,y=0,width=300,height=170)

        #image2
        img_1=Image.open("image/grocery.jfif")
        img_1=img_1.resize((300,170),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lb1_img_1=Label(self.root,image=self.photoimg_1)
        lb1_img_1.place(x=310,y=0,width=300,height=170)

        #image3
        img_2=Image.open("image/rice.jfif")
        img_2=img_2.resize((310,170),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lb1_img_2=Label(self.root,image=self.photoimg_2)
        lb1_img_2.place(x=620,y=0,width=310,height=170)

        #image4
        img_3=Image.open("image/snacks.jfif")
        img_3=img_3.resize((310,170),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        lb1_img_3=Label(self.root,image=self.photoimg_3)
        lb1_img_3.place(x=940,y=0,width=310,height=170)

        lb1_title=Label(self.root,text="BILLING  COUNTER",font=("times new roman",15,"bold"),bg="black",fg="white")
        lb1_title.place(x=0,y=175,width=1250,height=20)

        #Time
        """
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)    #1000=1 sec


        lbl = Label(lbl_title,font=('times new roman',16,'bold'),bg='black',fg='light green')
        lbl.place(x=0,y=0,width=120,height=45) 
        time()  
       """
       # self - if we want to use any variable/func inside class self is used 
       # with help self we can use anywhere the func
        

       #MAIN FRAME
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")   #groove =border style
        Main_Frame.place(x=0,y=200,width=1530,height=500)

        #Customer LABELFRAME    [in label frame we can add text,styles -color]
        Cust_Frame=LabelFrame(Main_Frame,text="Customer Details",font=("times new roman",13,"bold"),bg="white",fg="Red4")
        Cust_Frame.place(x=10,y=2,width=300,height=100)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",12,"bold"),width=22)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=("times new roman",12,"bold"),bg="white",text="Name",bd=4)
        self.lblCustName.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=22)
        self.txtCustName.grid(row=1,column=1,stick=W,padx=5,pady=2)

        #Product LABELFRAME
        Product_Frame=LabelFrame(Main_Frame,text="Product Details",font=("times new roman",13,"bold"),bg="white",fg="Red4")
        Product_Frame.place(x=315,y=3,width=500,height=100)
        
        #CATEGORY     using ttk.COMBOBOX
        self.lblCategory=Label(Product_Frame,font=("times new roman",13,"bold"),bg="white",text="Select Category",bd=4)
        self.lblCategory.grid(row=0,column=0,stick=W,padx=3,pady=1)
        
        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("times new roman",11,"bold"),width=21,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,stick=W,padx=3,pady=1)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #SUBCATEGORY
        self.lblSubCategory=Label(Product_Frame,font=("times new roman",13,"bold"),bg="white",text="SubCategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,stick=W,padx=3,pady=1)
        
        self.ComboSubCategory=ttk.Combobox(Product_Frame,textvariable=self.subcategory,value=[""],font=("times new roman",11,"bold"),width=21,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,stick=W,padx=3,pady=1)
        #self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.price)



        #Product
        '''   
        self.lblproduct=Label(Product_Frame,font=("times new roman",10,"bold"),bg="white",text="Product name",bd=4)
        self.lblproduct.grid(row=2,column=0,stick=W,padx=3,pady=1)
        
        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=("times new roman",10,"bold"),width=21,state="readonly")
        self.ComboProduct.grid(row=2,column=1,stick=W,padx=3,pady=1)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)'''

        #PRICE
        
        self.lblPrice=Label(Product_Frame,font=("times new roman",13,"bold"),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,stick=W,padx=3,pady=1)
        
        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("times new roman",11,"bold"),width=10,state="readonly")
        self.ComboPrice.grid(row=0,column=3,stick=W,padx=3,pady=1)

        #QTY
        self.lblQty=Label(Product_Frame,font=("times new roman",13,"bold"),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,stick=W,padx=3,pady=1)
        
        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("times new roman",11,"bold"),width=5)
        self.ComboQty.grid(row=1,column=3,stick=W,padx=3,pady=1)

        #MIDDLE FRAME
        Middleframe=Frame(Main_Frame,bd=10,bg="coral4")
        Middleframe.place(x=10,y=110,width=805,height=210)
        #image1
        imglogo=Image.open("image/gg.jpg")
        imglogo=imglogo.resize((300,180),Image.ANTIALIAS)
        self.photoimglogo=ImageTk.PhotoImage(imglogo)

        lb1_imglogo=Label(Middleframe,image=self.photoimglogo)
        lb1_imglogo.place(x=0,y=0,width=300,height=180)

        #image2
        #bg="coral4"
        
        img_13=Image.open("image/logo1.jpg")
        img_13=img_13.resize((430,150),Image.ANTIALIAS)
        self.photoimg_13=ImageTk.PhotoImage(img_13)

        lb1_img_13=Label(Middleframe,image=self.photoimg_13)
        lb1_img_13.place(x=320,y=0,width=430,height=150)

       #BILL AREA 
        #SEARCH
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=830,y=15,width=400,height=40)

        self.lblBill=Label(Search_Frame,font=("Arial",11,"bold"),fg="white",bg="Pink4",text="Bill Number")
        self.lblBill.grid(row=0,column=0,stick=W,padx=1)

        self.txt_EntrySearch=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("times new roman",11,"bold"),width=20)
        self.txt_EntrySearch.grid(row=0,column=1,stick=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("times new roman",11,"bold"),bg="IndianRed4",fg="white",width=12,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2,padx=1)

        #RIGHT FRAME BILL AREA
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Details",font=("times new roman",13,"bold"),bg="white",fg="Red4")
        RightLabelFrame.place(x=830,y=45,width=400,height=380)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",10,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #BILL COUNTER LABELFRAME
        Bottom_Frame=LabelFrame(Main_Frame,text="Order Total",font=("times new roman",13,"bold"),bg="white",fg="Red4")
        Bottom_Frame.place(x=0,y=320,width=810,height=115)

        #QTY
        self.lblSubtotal=Label(Bottom_Frame,font=("times new roman",11,"bold"),bg="white",text="SubTotal",bd=3)
        self.lblSubtotal.grid(row=0,column=0,stick=W,padx=5,pady=2)
        
        self.EntrySubtotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("times new roman",11,"bold"),width=14)
        self.EntrySubtotal.grid(row=0,column=1,stick=W,padx=5,pady=2)


        self.lbl_Tax=Label(Bottom_Frame,font=("times new roman",11,"bold"),bg="white",text="Tax",bd=4)
        self.lbl_Tax.grid(row=1,column=0,stick=W,padx=5,pady=2)
        
        self.txt_Tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("times new roman",11,"bold"),width=14)
        self.txt_Tax.grid(row=1,column=1,stick=W,padx=5,pady=2)
        

        self.lblAmountTotalotal=Label(Bottom_Frame,font=("times new roman",11,"bold"),bg="white",text="Total Amount",bd=4)
        self.lblAmountTotalotal.grid(row=2,column=0,stick=W,padx=5,pady=2)
        
        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("times new roman",11,"bold"),width=14)
        self.txtAmountTotal.grid(row=2,column=1,stick=W,padx=5,pady=2)

        #BUTTON FRAME
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height="1",text="Add to Cart",font=("times new roman",13,"bold"),bg="IndianRed4",fg="white",width=12,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0,padx=3,pady=2)

        self.BtnGeneratebill=Button(Btn_Frame,height="1",command=self.gen_bill,text="Generate Bill",font=("times new roman",13,"bold"),bg="IndianRed4",fg="white",width=12,cursor="hand2")
        self.BtnGeneratebill.grid(row=0,column=2,padx=3,pady=2)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height="1",text="Save",font=("times new roman",13,"bold"),bg="IndianRed4",fg="white",width=12,cursor="hand2")
        self.BtnSave.grid(row=0,column=3,padx=3,pady=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height="1",text="Print",font=("times new roman",13,"bold"),bg="IndianRed4",fg="white",width=12,cursor="hand2")
        self.BtnPrint.grid(row=1,column=3,padx=3,pady=2)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height="1",text="Clear",font=("times new roman",13,"bold"),bg="IndianRed4",fg="white",width=12,cursor="hand2")
        self.BtnClear.grid(row=1,column=0,padx=3,pady=2)

        self.BtnExit=Button(Btn_Frame,command=self.reg ,height="1",text="Exit",font=("times new roman",13,"bold"),bg="IndianRed4",fg="white",width=12,cursor="hand2")
        self.BtnExit.grid(row=1,column=2,padx=3,pady=2)

        self.welcome()

        self.l=[]

    #************FUNCTION DECLARATION**************

    #databse function declaration
    
    def reg(self):
        name = self.c_name.get()
        phone = self.c_phon.get()
        conn = sqlite3.connect("grocery.db")
        c=conn.cursor()
        c.execute("INSERT INTO details VALUES ('"+name+"','"+phone+"')")
        conn.commit()
        conn.close()
        
    ##WELCOME PAGE
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t Welcome to Nature's Basket")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        #self.textarea.insert(END,f"\n Customer Email :{self.c_email.get()}")

        self.textarea.insert(END,"\n=====================================================")
        self.textarea.insert(END,"\n Products \t\t\tQty\t\tPrice")
        self.textarea.insert(END,"\n=====================================================\n\n")

 #TAX
    

    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m) 
        if self.ComboSubCategory.get()=="": 
            messagebox.showerror("Error","Please select the product") 
        else: 
            self.textarea.insert(END,f"\n {self.ComboSubCategory.get()}\t\t\t{self.qty.get()}\t\t{self.m}") 
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l)))) 
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100))) 
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - self.prices.get()))*Tax)/100))))  


    def gen_bill(self): 
      if self.ComboSubCategory.get()=="": 
          messagebox.showerror("Error","Please Add to cart the product") 
      else: 
          text=self.textarea.get(10.0,(10.0+float(len(self.l)))) 
          self.welcome() 
          self.textarea.insert(END,text) 
          self.textarea.insert(END,"\n\n===================================================") 
          self.textarea.insert(END,f"\n Sub Amount:\t\t{self.sub_total.get()}") 
          self.textarea.insert(END,f"\n Tax Amount:\t\t{self.tax_input.get()}") 
          self.textarea.insert(END,f"\n Total Amount:\t\t{self.total.get()}")
          self.textarea.insert(END,f"\n===================================================")

          
         
    def save_bill(self):
      op=messagebox.askyesno("Save Bill","Do you want to save the bill") 
      if op>0: 
          self.bill_data=self.textarea.get(1.0,END) 
          f1=open('bills/'+str(self.bill_no.get())+".txt",'w') 
          f1.write(self.bill_data) 
          op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved successfully") 
          f1.close()
          
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")


    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        #self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()





    def Categories(self,event=""):
        if self.Combo_Category.get()=="Fruits":
            self.ComboSubCategory.config(value=self.SubCatFruits)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Vegetables":
            self.ComboSubCategory.config(value=self.SubCatVeggie)
            self.ComboSubCategory.current(0)
        
        if self.Combo_Category.get()=="Dairy":
            self.ComboSubCategory.config(value=self.SubCatDairy)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Bread/Bakery":
            self.ComboSubCategory.config(value=self.SubCatBread)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Cereals/Pulses":
            self.ComboSubCategory.config(value=self.SubCatCereals)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Snacks":
            self.ComboSubCategory.config(value=self.SubCatSnacks)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Beverages":
            self.ComboSubCategory.config(value=self.SubCatBev)
            self.ComboSubCategory.current(0) 

    
    #******
    def price(self,event=""):
        #FRUITS  ["Apples","Mangoes","Bananas","Oranges","Watermelon"]
        
        if self.ComboSubCategory.get()=="Apples":
            self.ComboPrice.config(value=self.price_Apples)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboSubCategory.get()=="Bananas":
            self.ComboPrice.config(value=self.price_banana)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboSubCategory.get()=="Oranges":
            self.ComboPrice.config(value=self.price_Orange)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboSubCategory.get()=="Mangoes":
            self.ComboPrice.config(value=self.price_Mangoes)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboSubCategory.get()=="Watermelon":
            self.ComboPrice.config(value=self.price_watermelon)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        #Veggie=["Potato","Tomato","Green chillies","Onion"]
        if self.ComboSubCategory.get()=="Potato":
            self.ComboPrice.config(value=self.price_potato)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboSubCategory.get()=="Tomato":
            self.ComboPrice.config(value=self.price_tomato)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboSubCategory.get()=="Onion":
            self.ComboPrice.config(value=self.price_onion)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboSubCategory.get()=="Green chillies":
            self.ComboPrice.config(value=self.price_green)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        #Dairy=["Milk","Cheese","Egg","Paneer"]
        if self.ComboSubCategory.get()=="Milk":
            self.ComboPrice.config(value=self.price_Milk)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboSubCategory.get()=="Cheese":
            self.ComboPrice.config(value=self.price_cheese)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboSubCategory.get()=="Egg":
            self.ComboPrice.config(value=self.price_egg)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboSubCategory.get()=="Paneer":
            self.ComboPrice.config(value=self.price_paneer)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        #Bread=["White bread","Brown bread","Multi grain","French bread"]
        if self.ComboSubCategory.get()=="Garlic bread":
            self.ComboPrice.config(value=self.price_garlic)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboSubCategory.get()=="Brown bread":
            self.ComboPrice.config(value=self.price_brown)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboSubCategory.get()=="Multi grain":
            self.ComboPrice.config(value=self.price_multi)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboSubCategory.get()=="French bread":
            self.ComboPrice.config(value=self.price_french)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Cereals=["Rice","Wheat","Oats","Beans","Dry peas"]
        if self.ComboSubCategory.get()=="Rice":
            self.ComboPrice.config(value=self.price_rice)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboSubCategory.get()=="Wheat":
            self.ComboPrice.config(value=self.price_wheat)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboSubCategory.get()=="Oats":
            self.ComboPrice.config(value=self.price_oats)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboSubCategory.get()=="Beans":
            self.ComboPrice.config(value=self.price_beans)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboSubCategory.get()=="Dry peas":
            self.ComboPrice.config(value=self.price_drypeas)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Snacks=["Lays","Popcorn","Chocolates","Nachos"]
        if self.ComboSubCategory.get()=="Lays":
            self.ComboPrice.config(value=self.price_lays)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboSubCategory.get()=="Popcorn":
            self.ComboPrice.config(value=self.price_popcorn)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboSubCategory.get()=="Chocolates":
            self.ComboPrice.config(value=self.price_Chocolates)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboSubCategory.get()=="Nachos":
            self.ComboPrice.config(value=self.price_nachos)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Bev=["Pepsi","Fruit juice","Cold Coffee"]
        if self.ComboSubCategory.get()=="Pepsi":
            self.ComboPrice.config(value=self.price_pepsi)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboSubCategory.get()=="Fruit juice":
            self.ComboPrice.config(value=self.price_fruitjuice)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboSubCategory.get()=="Cold Coffee":
            self.ComboPrice.config(value=self.price_Coldcoffee)
            self.ComboPrice.current(0)
            self.qty.set(1)




if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()       #mainloop will keep the window till we dont close it.

