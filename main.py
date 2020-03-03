import tkinter as tk
from tkinter import filedialog
import json
import numpy as np
import os
import pandas as pd

with open('config.json', 'r') as f:
    params = json.load(f)['params']


def get_extension(st):
    '''this function is use for getting a file extension from file addresses
    or file names'''

    def str_reverse(st):
        st = list(st)
        st.reverse()
        return ''.join(st)

    st = str_reverse(st)
    string = ''
    for i in st:
        string += i
        if i == '.':
            break
    return str_reverse(string)

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        # self.tab_control = tkinter.ttk.Notebook()  # tab object initialization
        # self.tab_control.pack(expan=10, fill='both')
        height = params['window_height']
        width = params['window_width']
        self.geometry(f"{height}x{width}")
        self.title(params['application name'])
        self.config(bg=params["background color"])



    def error_object(self):
        self.error = tk.StringVar()
        self.error_widget = tk.Label(self, textvariable=self.error, fg='red', bg=params["background color"], font='2')
        self.error_widget.pack(side=tk.BOTTOM)

class Product_entry():
    def __init__(self,parent):

        # body object ########################
        self.body = tk.Frame(parent, height = 500, width =500)
        self.body.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.img_address = tk.StringVar()

        self.product_name(self.body,'Product Name')
        self.quantity(self.body,'Quantity')
        self.purchase_price(self.body,'Purchase Price')
        self.sell_price(self.body,'Sell Price')
        self.product_image(self.body,'Select Image')
        self.add_product_button(self.body,'Add Product')
        self.wholesaler_name(self.body,'Wholesalers')

        # footer objects ###################
        self.footer = tk.Frame(parent,bg='light grey',height = 20)
        self.footer.pack(side='bottom', fill='x' )
        self.error = tk.StringVar()
        tk.Label(self.footer, textvariable=self.error, font='time 13 bold',bg='light grey').pack()


    def product_name(self,parent,name):
        frame = tk.Frame(parent,padx=2,pady=20)
        frame.grid(row=0,columnspan=2,padx=10)
        tk.Label(frame, text=f'{name}', font='arial 12 bold').grid(row=0,column=0)
        self.item_name = tk.Entry(frame,font='arial 13',bg='light grey')
        self.item_name.grid(row=0,column=1,ipadx=60,)

    def quantity(self,parent,name):
        frame = tk.Frame(parent,padx=2,pady=20)
        frame.grid(row=1,column=0)
        tk.Label(frame, text=f'{name}', font='arial 12 bold').grid(row=0,column=0)
        self.item_quantity = tk.Entry(frame,font='arial 12',bg='light grey',width='6')
        self.item_quantity.grid(row=0,column=1,)

    def purchase_price(self,parent,name):
        frame = tk.Frame(parent,padx=2,pady=20)
        frame.grid(row=1,column=1)
        tk.Label(frame, text=f'{name}', font='arial 12 bold').grid(row=0,column=0)
        self.item_purchase_price = tk.Entry(frame,font='arial 12',bg='light grey',width='6')
        self.item_purchase_price.grid(row=0,column=1)

    def sell_price(self,parent,name):
        frame = tk.Frame(parent,padx=2,pady=20)
        frame.grid(row=2,column=0)
        tk.Label(frame, text=f'{name}', font='arial 12 bold').grid(row=0,column=0)
        self.item_sell_price = tk.Entry(frame,font='arial 12',bg='light grey',width='6')
        self.item_sell_price.grid(row=0,column=1)

    def product_image(self,parent,name):
        frame = tk.Frame(parent,padx=2,pady=20)
        frame.grid(row=2,column=1)
        tk.Label(frame, text=f'{name}', font='arial 12 bold').grid(row=0,column=0)
        tk.Button(frame,text='Browse',height=1,width=6,font='arial 12',bg='light grey',command=self.browse_image).grid(row=0,column=1)

    def add_product_button(self,parent,name):
        frame = tk.Frame(parent,padx=2,pady=20)
        frame.grid(row=4,columnspan=2)
        tk.Button(frame,text=f'{name}',font='arial 12',bg='light grey',command=self.add_product_detail).grid(row=0,column=0)

    def wholesaler_name(self,parent, name):
        frame = tk.Frame(parent, padx=2, pady=20)
        frame.grid(row=3, columnspan=2)

        tk.Label(frame, text=f'{name}', font='arial 12 bold').grid(row=0, column=0,padx=2)

        self.w_seller1 = tk.StringVar()
        tk.Entry(frame, font='arial 12', bg='light grey', width='9',textvariable=self.w_seller1).grid(row=0, column=1,padx=2)
        self.w_seller2 = tk.StringVar()
        tk.Entry(frame, font='arial 12', bg='light grey', width='9',textvariable=self.w_seller2).grid(row=0, column=2,padx=2)
        self.w_seller3 = tk.StringVar()
        tk.Entry(frame, font='arial 12', bg='light grey', width='9',textvariable=self.w_seller3).grid(row=0, column=3,padx=2)
        self.w_seller_self = tk.IntVar()
        tk.Checkbutton(frame, text='self', font='arial 12 bold',variable=self.w_seller_self).grid(row=0, column=4)


    def add_product_detail(self):
        database_path = params['database_path']
        product_inventory_detail = 'Inventory Data'

        product_dir_name = self.item_name.get()
        # columns
        item_name = self.item_name.get()
        item_purchase_price = self.item_purchase_price.get()
        item_sell_price = self.item_sell_price.get()
        item_quantity = self.item_quantity.get()
        whole_seller1 = self.w_seller1.get()
        whole_seller2 = self.w_seller2.get()
        whole_seller3 = self.w_seller3.get()
        self_seller = self.w_seller_self.get()

        # os.mkdir(f"{database_path}\{product_dir_name}")
        #
        # image_path = self.img_address.get()
        # file_save_path = f'{database_path}\{product_dir_name}'
        # self.add_image( image_path, file_save_path, "any image.jpg")

        arr = np.array([item_name, item_quantity, item_purchase_price, item_sell_price, self_seller, whole_seller1, whole_seller2, whole_seller3])
        # self.save_product_data(database_path, product_inventory_detail, arr)
        os.system("git init")
        os.system("git add .")
        os.system("git commit -m 'a file added'")
        # print(read)


    def push_data_to_server(self):
        os.system("git add .")
        os.system("git commit -m ")
        os.system("")
        os.system("")


    def get_product_data(self, file_path, file_name):
        os.chdir(rf'{file_path}')
        arr = np.load(file_name)
        return arr.f.arr_0

    def save_product_data(self,file_path,file_name,arr_object):
        os.chdir(rf'{file_path}')
        arr = np.load(file_name)
        arr = arr.f.arr_0
        arr = np.vstack()
        np.savez_compressed(file_name, arr)

    def add_image(self, img_receive_path, img_save_path, img_name):
        '''
        :param img_receive_path: this is image file path to get the image.
        :param img_save_path: this is the path where the image will be save
        :param img_name: this is the name of the image to save as file name
        :return: nothing
        '''
        from PIL import Image
        img = Image.open(rf"{img_receive_path}")
        img.save(rf"{img_save_path}\{img_name}")

    def browse_image(self,):
        from tkinter import filedialog
        file = filedialog.askopenfilename(filetype=(('Image file', '*.png;*.jpg;*jpej;*jfif'),('All files', '*.*')))
        self.img_address.set(file)
        print(file)

if __name__ == '__main__':

    gui = App()
    Product_entry(gui)
    gui.mainloop()
