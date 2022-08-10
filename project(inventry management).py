from tkinter import*
import math, random
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = ("#003366")
        title = Label(self.root, text="Billing Software", bd=12, bg=bg_color,
                      relief=GROOVE, fg="white", font=("times new roman", 30, "bold"), pady=2).pack()

        ##                   variable   ###############
        ############  Cosmeic  ########################
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.lotion = IntVar()

        ######## grocery  ####################
        self.Rice = IntVar()
        self.tea = IntVar()
        self.Refined = IntVar()
        self.sugar = IntVar()
        self.Mustard_oil = IntVar()
        self.dal = IntVar()

        ###########  Cold drinks ############
        self.coca_cola = IntVar()
        self.maaza = IntVar()
        self.pepsi = IntVar()
        self.sting = IntVar()
        self.thumbs_up = IntVar()
        self.limca = IntVar()

        ##########Total Product  & Tax variavle ###
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()

        self.cosmetic_tax = IntVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()

        ##### Customer #################
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=(
            "times new roman", 15, "bold"), fg="red", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="customerName", bg=bg_color, font=(
            "time new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, fg="black",
                          font="arial 15", bd=6, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, font=(
            "time new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phon, fg="black",
                         font="arial 15", bd=6, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="customer Bill", bg=bg_color, font=(
            "time new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.bill_no, fg="black",
                           font="arial 15", bd=6, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", width=10, textvariable=self.search_bill,
                          bd=7, font="arial 12 bold").grid(row=0, column=6, padx=10, pady=10)

        ###Cosmetic frame#################################
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=(
            "times new roman", 15, "bold"), fg="red", bg=bg_color)
        F2.place(x=5, y=180, relwidth=350, height=380)

        bath_lbl = Label(F2, text="bath Soap", font=("times new roman ", 16, "bold"),
                         bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10, textvariable=self.soap, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        cream_lbl = Label(F2, text=" cream", font=("times new roman ", 16, "bold"),
                          bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        cream_txt = Entry(F2, width=10, textvariable=self.face_cream, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        lotion_lbl = Label(F2, text="body lotion", font=("times new roman ", 16, "bold"),
                           bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        lotion_txt = Entry(F2, width=10, textvariable=self.face_wash, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        spry_lbl = Label(F2, text="hair spray", font=("times new roman ", 16, "bold"),
                         bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        spry_txt = Entry(F2, width=10, textvariable=self.spray, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        face_w_lbl = Label(F2, text="face wash", font=("times new roman ", 16, "bold"),
                           bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        face_w_txt = Entry(F2, width=10, textvariable=self.gel, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        hair_g_lbl = Label(F2, text="hair gel", font=("times new roman ", 16, "bold"),
                           bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        hair_o_txt = Entry(F2, width=10, textvariable=self.lotion, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        ###   Grocery Frame  #################################
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=(
            "times new roman", 15, "bold"), fg="red", bg=bg_color)
        F3.place(x=340, y=180, relwidth=350, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman ", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.Rice, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(F3, text="tea", font=("times new roman ", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.tea, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3_lbl = Label(F3, text="Refined", font=("times new roman ", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.Refined, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(F3, text="Sugar", font=("times new roman ", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10, textvariable=self.sugar, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(F3, text="Mustard oil", font=("times new roman ", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.Mustard_oil, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(F3, text="Dal", font=("times new roman ", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.dal, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        ###           Cold drink    #################################
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold drinks", font=(
            "times new roman", 15, "bold"), fg="red", bg=bg_color)
        F4.place(x=650, y=180, relwidth=350, height=380)

        c1_lbl = Label(F4, text="coca cola", font=("times new roman ", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10, textvariable=self.coca_cola, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        c2_lbl = Label(F4, text="maaza", font=("times new roman ", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10, textvariable=self.maaza, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        c3_lbl = Label(F4, text="pepsi", font=("times new roman ", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10, textvariable=self.pepsi, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        c4_lbl = Label(F4, text="Sting", font=("times new roman ", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10, textvariable=self.sting, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        c5_lbl = Label(F4, text="Thumbs up", font=("times new roman ", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10, textvariable=self.thumbs_up, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        c6_lbl = Label(F4, text="Limca", font=("times new roman ", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10, textvariable=self.limca, font=(
            "times new roman ", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        ####   BILL Area ############
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, relwidth=200, height=380, width=350)
        # F5=Frame(self.root,bd=10,relief=GROOVE)
        # F5.place(x=1010,y=180,relwidth=200,width=350,height=380)
        bill_title = Label(F5, text="Bill Area", font=(
            "arial ", 15, "bold"), bd=7, relief=GROOVE).pack(fill=X)

        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(comman=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH)

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill menu", font=(
            "times new roman", 15, "bold"), fg="red", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=200)

        m1 = Label(F6, text="Total cosmetic price", bg=bg_color, fg="white", font=(
            "times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold",
                       bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2 = Label(F6, text="Total Grocery price", bg=bg_color, fg="white", font=(
            "times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold",
                       bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3 = Label(F6, text="Total cold drink price", bg=bg_color, fg="white", font=(
            "times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price,
                       font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)
        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=650, width=550, height=105)

        total_btn = Button(btn_F, text="total", command=self.total, bg="cadetblue", fg="white",
                           bd=5, pady=15, width=11, font="arial 12").grid(row=0, column=0, padx=5, pady=5)
        Gbill_btn = Button(btn_F, text="Gbill",command=self.bill_area, bg="cadetblue", fg="white",
                           bd=5, pady=15, width=11, font="arial 12").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear",command=self.clear_data, bg="cadetblue", fg="white", bd=5,
                           pady=15, width=11, font="arial 12").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit",command=self.Exit_app, bg="cadetblue", fg="white", bd=5,
                          pady=15, width=11, font="arial 12").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()
#   declaartion of Variable***********************
    def total(self):
        
        self.c_s_p = (self.soap.get()*40)
        self.c_fc_p = (self.face_cream.get()*90)
        self.c_fw_p = (self.face_wash.get()*140)
        self.c_spr_p = (self.spray.get()*95)
        self.c_gl_p = (self.gel.get()*75)
        self.c_lo_p = (self.lotion.get()*130)

        self.total_cosmetic_price = float(
            self.c_s_p +
            self.c_fc_p +
            self.c_fw_p +
            self.c_spr_p +
            self.c_gl_p +
            self.c_lo_p)

        self.cosmetic_price.set('Rs.'+str(self.total_cosmetic_price))
        
        #**** grocery *****
        self.g_r_p = (self.Rice.get()*30)
        self.g_t_p = (self.tea.get()*60)
        self.g_Re_p = (self.Refined.get()*90)
        self.g_Mo_p = (self.Mustard_oil.get()*75)
        self.g_s_p = (self.sugar.get()*38)
        self.g_d_p = (self.dal.get()*65)

        self.total_grocery_price = float(
            self.g_r_p +
            self.g_t_p +
            self.g_Re_p +
            self.g_Mo_p +
            self.g_s_p +
            self.g_d_p)

        self.grocery_price.set('Rs.'+str(self.total_grocery_price))
      
        

        #**cold drinks***

        self.cd_cc_p = (self.coca_cola.get()*40)
        self.cd_mz_p = (self.maaza.get()*90)
        self.cd_ps_p = (self.pepsi.get()*30)
        self.cd_st_p = (self.sting.get()*25)
        self.cd_th_p = (self.thumbs_up.get()*40)
        self.cd_li_p = (self.limca.get()*75)

        self.total_cold_drinks_price = float(
            self.cd_cc_p +
            self.cd_mz_p +
            self.cd_ps_p +
            self.cd_st_p +
            self.cd_th_p +
            self.cd_li_p)

        self.cold_drinks_price.set('Rs.'+str(self.total_cold_drinks_price))
       
        self.Total_bill =float(
                                    self.total_cosmetic_price+
                                        self.total_grocery_price+
                                           self.total_cold_drinks_price)
        
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, " \twelcome webcode ")
        self.txtarea.insert(END, f"\nBill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\n customer name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number:{self.c_phon.get()} ")
        self.txtarea.insert(END, f"\n ************ ")
        self.txtarea.insert(END, f"\n Product\t\tQty\t\tPrice ")
        self.txtarea.insert(END, f"\n ************ ")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details are must")
        else:    
             self.welcome_bill()
        if self.soap.get() != 0:
           self.txtarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
        if self.face_cream.get() != 0:
           self.txtarea.insert(END, f"\n Face cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
        if self.lotion.get() != 0:
           self.txtarea.insert(END, f"\n Lotion\t\t{self.lotion.get()}\t\t{self.c_lo_p}")
        if self.spray.get() != 0:
           self.txtarea.insert(END, f"\n Spray\t\t{self.spray.get()}\t\t{self.c_spr_p}")
        if self.face_wash.get() != 0:
           self.txtarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
        if self.gel.get() != 0:
           self.txtarea.insert(END, f"\n Gel\t\t{self.gel.get()}\t\t{self.c_gl_p}")
        


        if self.Rice.get() != 0:
           self.txtarea.insert(END, f"\n Rice\t\t{self.Rice.get()}\t\t{self.g_r_p}")
        if self.tea.get() != 0:
           self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")
        if self.Refined.get() != 0:
           self.txtarea.insert(END, f"\n Refined\t\t{self.Refined.get()}\t\t{self.g_Re_p}")
        if self.sugar.get() != 0:
           self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
        if self.Mustard_oil.get() != 0:
           self.txtarea.insert(END, f"\n Mustard Oil\t\t{self.Mustard_oil.get()}\t\t{self.g_Mo_p}")
        if self.dal.get() != 0:
           self.txtarea.insert(END, f"\n Dal\t\t{self.dal.get()}\t\t{self.g_d_p}")

        if self.coca_cola.get() != 0:
           self.txtarea.insert(END, f"\n Coca cola\t\t{self.coca_cola.get()}\t\t{self.cd_cc_p}")
        if self.maaza.get() != 0:
           self.txtarea.insert(END, f"\n maaza\t\t{self.maaza.get()}\t\t{self.cd_mz_p}")
        if self.pepsi.get() != 0:
           self.txtarea.insert(END, f"\n pepsi\t\t{self.pepsi.get()}\t\t{self.cd_ps_p}")
        if self.sting.get() != 0:
           self.txtarea.insert(END, f"\n sting\t\t{self.sting.get()}\t\t{self.cd_st_p}")
        if self.thumbs_up.get() != 0:
           self.txtarea.insert(END, f"\n thumbs_up\t\t{self.thumbs_up.get()}\t\t{self.cd_th_p}")
        if self.limca.get() != 0:
           self.txtarea.insert(END, f"\n limca\t\t{self.limca.get()}\t\t{self.cd_li_p}")
           
           
        self.txtarea.insert(END,f"\n---------------------------------------------------")
        self.txtarea.insert(END,f"\n Total\t\t\t\t\t{self.Total_bill}")
        self.txtarea.insert(END,f"\n---------------------------------------------------")   
    def clear_data(self):
          ############  Cosmeic  ########################
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gel.set(0)
        self.lotion.set(0)

        ######## grocery  ####################
        self.Rice.set(0) 
        self.tea.set(0) 
        self.Refined.set(0) 
        self.sugar.set(0) 
        self.Mustard_oil.set(0) 
        self.dal.set(0) 

        ###########  Cold drinks ############
        self.coca_cola.set(0) 
        self.maaza.set(0)
        self.pepsi.set(0)
        self.sting.set(0) 
        self.thumbs_up .set(0)
        self.limca .set(0)

        ##########Total Product  & Tax variavle ###
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()

      
        ##### Customer #################
        self.c_name .set("")
        self.c_phon .set("")
        self.bill_no .set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill .set("")
        self.welcome_bill()
        
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit") 
        if op>0:
            self.root.destroy()
          

root = Tk()
obj =Bill_App(root)
root.mainloop()