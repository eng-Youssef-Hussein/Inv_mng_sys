'''
WHAT IS THE PROJECT ?? 
The project is inventory management system
[1]     The project include sales page
-----   sales page is to manage the sales and make the list of sales at the day
[2]     The project include item page
-----   The item page is to include the goods list you bought it
[3]     make page include returns items
-----   to include the returns item from client
[4]     make page include clients information like [phone number , client name , items of client]
'''

from customtkinter import *
from tkinter import *
from tkinter import ttk
import sqlite3



window = CTk()
window.geometry('900x900')
set_appearance_mode('System')

#                                                   START FUNCTIONS CONTAINER


# open_daily_report_window function
def open_daily_report_window():
    daily_report_window = CTkToplevel()
    daily_report_window.geometry('900x900')
    set_appearance_mode('System')
    








    #           CREATE THE DATA BASE TREEVIEW LIST

    #   first i will create the frame
    tree_view_frame = CTkFrame(daily_report_window)
    tree_view_frame.place(relwidth =1, relheight=1)
    #   after creating the frame i create the scroll bar
    scroll_bar  = ttk.Scrollbar(tree_view_frame)
    scroll_bar.pack(side=RIGHT, fill=Y)

    #ADD STYLE
    style = ttk.Style()
    #CONFIGURE THE TREEVIEW COLOR
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight =40 ,font = ("Arial", 10, "bold"))
    style.map("Treeview", background = [("selected" , "#347083")])
    #   now i will create the treeview element

    items_list = ttk.Treeview(tree_view_frame, yscrollcommand=scroll_bar, selectmode='extended',style='Treeview')
    items_list.place(relheight=1, relwidth=1)

    #    HERE IS GIVINE A FUNCTION TO SCROLLBAR
    scroll_bar.config(command = sales_list.yview)

    #   HERE IS CREATING THE TREEVIEW COLUMNS
    items_list['columns'] = ('Barcode','ItemName','Brand','Material','Quantity', 'WarehouseLocation','PurchesPrice','SellingPrice', 'Discount', 'ProfitMaregin')

    items_list.column('#0',width=0 ,stretch=NO)
    items_list.column('Barcode', width=120, anchor=W)
    items_list.column('ItemName', width=120,anchor='center')
    items_list.column('Discount', width=120,anchor='center')
    items_list.column('ProfitMaregin', width=120,anchor='center')
    items_list.column('Quantity',width=120 , anchor='center')

    items_list.column('#0', anchor=W)
    items_list.heading('Barcode', text='Barcode', anchor=W)
    items_list.heading('ItemName', text='ItemName', anchor='center')
    items_list.heading('Discount', text='Discount', anchor='center')
    items_list.heading('ProfitMaregin', text='ProfitMaregin', anchor='center')
    items_list.heading('Quantity', text='Quantity', anchor='center')



    daily_report_window.mainloop()




def inventory_open_window():
    

    inventory_window = CTkToplevel()
    inventory_window.geometry('900x900')
    set_appearance_mode('System')







    #       CREATE THE FIELDS HERE
    # [01]  inventory name field
    inventory_name_field = CTkEntry(inventory_window, placeholder_text= 'Inventory Name', width=290, height=40, font=('Arial', 17))
    inventory_name_field.grid(column = 0 , row = 0, padx=30, pady=20)
    # [02]  inventory address field
    inventory_address_field = CTkEntry(inventory_window, placeholder_text= 'Inventory Address', width=290, height=40, font=('Arial', 17))
    inventory_address_field.grid(column =1 , row = 0, padx=30, pady=20)
    # [03]  inventory manager name field
    inventory_manger_name_field = CTkEntry(inventory_window, placeholder_text= 'Manager Name', width=290, height=40, font=('Arial', 17))
    inventory_manger_name_field.grid(column =2, row = 0, padx=30, pady=20)
    # [03]  inventory phone number
    inventory_phone_number_field = CTkEntry(inventory_window, placeholder_text= 'Phone Number', width=290, height=40, font=('Arial', 17))
    inventory_phone_number_field.grid(column =3, row = 0, padx=30, pady=20)








    ####                CREATE THE BUTTONS [SUBMIT , UPDATE , DELETE]
    inventory_page_submit_button = CTkButton(inventory_window, text='Submit', height=40, fg_color='#467D35', font=('Arial', 17, 'bold'))
    inventory_page_submit_button.grid(column = 4, row = 0, padx=30, pady=20)
    ##      UPDATE BUTTON
    inventory_page_update_button = CTkButton(inventory_window, text='Update', height=40, fg_color='#B59460', font=('Arial', 17, 'bold'))
    inventory_page_update_button.grid(column = 5, row = 0, padx=30, pady=20)
    ##      DELETE BUTTON
    inventory_page_delete_button = CTkButton(inventory_window, text='Delete', height=40, fg_color= '#723637', font=('Arial', 17, 'bold'))
    inventory_page_delete_button.grid(column = 5, row = 1, padx=30, pady=20)







    #           CREATE THE DATA BASE TREEVIEW LIST

    #   first i will create the frame
    tree_view_frame = CTkFrame(inventory_window)
    tree_view_frame.place(relwidth =1, y =200, relheight=1)
    #   after creating the frame i create the scroll bar
    scroll_bar  = ttk.Scrollbar(tree_view_frame)
    scroll_bar.pack(side=RIGHT, fill=Y)

    #ADD STYLE
    style = ttk.Style()
    #CONFIGURE THE TREEVIEW COLOR
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight =40 ,font = ("Arial", 10, "bold"))
    style.map("Treeview", background = [("selected" , "#347083")])
    #   now i will create the treeview element

    inventory_list = ttk.Treeview(tree_view_frame, yscrollcommand=scroll_bar, selectmode='extended',style='Treeview')
    inventory_list.place(relheight=1, relwidth=1)

    #    HERE IS GIVINE A FUNCTION TO SCROLLBAR
    scroll_bar.config(command = sales_list.yview)

    #   HERE IS CREATING THE TREEVIEW COLUMNS
    inventory_list['columns'] = ('ID','Name','Address','ManagerName', 'PhoneNumber')

    inventory_list.column('#0',width=0 ,stretch=NO)
    inventory_list.column('ID', width=120, anchor=W)
    inventory_list.column('Name', width=120,anchor='center')
    inventory_list.column('Address', width=120,anchor='center')
    inventory_list.column('ManagerName', width=120,anchor='center')
    inventory_list.column('PhoneNumber', width=120,anchor='center')



    inventory_list.column('#0', anchor=W)
    inventory_list.heading('ID', text='ID', anchor=W)
    inventory_list.heading('Name', text='Name', anchor='center')
    inventory_list.heading('Address', text='Address', anchor='center')
    inventory_list.heading('ManagerName', text='ManagerName', anchor='center')
    inventory_list.heading('PhoneNumber', text='PhoneNumber', anchor='center')







    inventory_window.mainloop()




def items_window():
    clothing_materials = [
    "Cotton","Wool",
    "Silk","Linen","Polyester",
    "Nylon","Rayon","Spandex",
    "Denim","Leather","Suede",
    "Fleece","Acrylic","Velvet",
    "Satin","Chiffon","Tweed",
    "Corduroy","Jersey","Canvas",
    "Tulle","Bamboo Fabric","Hemp Fabric",
    "Modal","Lyocell","Viscose",
    "Microfiber","Mesh","Neoprene"
    ]

    def database_query():
        conn = sqlite3.connect("inventoryDB.db")
        cursor = conn.cursor()
        cursor.execute('select * from items')
        records = cursor.fetchall()
        count = 0
        for record in records:
            count +=1
            items_list.insert(parent='', text='',index='end',iid=count, values=(record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10]))
        conn.commit()
        conn.close()


    item_toplevel_window = CTkToplevel()
    item_toplevel_window.title('Items')
    item_toplevel_window.geometry('900x900')
    set_appearance_mode('System')

    # here i will write the functions of item page
    def submit_button_function():

        #       THIS CONTENT TO COLLECT THE VALUES OF ENTRIES
        barcode_get=barcode_entry.get()
        item_name_get=item_name_entry.get()
        brand_get=brand_entry.get()
        material_get=material_optionmenu.get()
        quantity_get=quantity_entry.get()
        warehouse_name_get=warehouse_location_entry.get()
        purches_get=create_purches_entry.get()
        selling_get=selling_price_entry.get()
        discount_get=discount_entry.get()
        supplier_get =supplier_entry.get()

        #       create the connection with data
        conn = sqlite3.connect('inventoryDB.db')
        cursor = conn.cursor()
        cursor.execute("insert into items ('barcode','item_name','brand','material','quantity','warhouse_name','purchase_price','selling_price','discount','supplier_name') values(?,?,?,?,?,?,?,?,?,?)",
        (barcode_get,item_name_get,brand_get,material_get,quantity_get,warehouse_name_get,purches_get,selling_get,discount_get,supplier_get))
        conn.commit()
        conn.close()
        items_list.insert('', 'end', values=(
        barcode_get, item_name_get, brand_get, material_get, quantity_get, 
        warehouse_name_get, purches_get, selling_get, discount_get, supplier_get
        ))

        barcode_entry.delete(0, END)
        item_name_entry.delete(0, END)
        brand_entry.delete(0, END)
        quantity_entry.delete(0, END)
        warehouse_location_entry.delete(0, END)
        create_purches_entry.delete(0, END)
        selling_price_entry.delete(0, END)
        discount_entry.delete(0, END)
        supplier_entry.delete(0, END)
        
        
    def select_record(e):
        barcode_entry.delete(0, END)
        item_name_entry.delete(0, END)
        brand_entry.delete(0, END)
        quantity_entry.delete(0, END)
        warehouse_location_entry.delete(0, END)
        create_purches_entry.delete(0, END)
        selling_price_entry.delete(0, END)
        discount_entry.delete(0, END)
        supplier_entry.delete(0, END)

        select = items_list.focus()
        values = items_list.item(select,'values')

        barcode_entry.insert(0,values[0])
        item_name_entry.insert(0,values[1])
        brand_entry.insert(0,values[2])
        quantity_entry.insert(0,values[4])
        warehouse_location_entry.insert(0, values[5])
        create_purches_entry.insert(0, values[5])
        selling_price_entry.insert(0, values[7])
        discount_entry.insert(0, values[8])
        supplier_entry.insert(0, values[9])



    def update_button_function():
        select = items_list.focus()  # الحصول على العنصر المحدد
        barcode_value = barcode_entry.get()
        # **🔄 تحديث العنصر في Treeview مباشرة**
        items_list.item(select, values=(
            barcode_entry.get(),
            item_name_entry.get(),
            brand_entry.get(),
            material_optionmenu.get(),
            quantity_entry.get(),
            warehouse_location_entry.get(),
            create_purches_entry.get(),
            selling_price_entry.get(),
            discount_entry.get(),
            supplier_entry.get()
        ))

        # تحديث قاعدة البيانات
        update_connection = sqlite3.connect('inventoryDB.db')
        update_cursor = update_connection.cursor()

        update_cursor.execute("""
            UPDATE items
            SET item_name=?, brand=?, material=?,quantity=?, warhouse_name=?,  purchase_price=?, selling_price=?, discount=?, supplier_name=?
            WHERE barcode=?
        """, (
            item_name_entry.get(),
            brand_entry.get(),
            material_optionmenu.get(),
            quantity_entry.get(),
            warehouse_location_entry.get(),
            create_purches_entry.get(),
            selling_price_entry.get(),
            discount_entry.get(),
            supplier_entry.get(),
            barcode_entry.get()  # تأكد أنه آخر قيمة في WHERE
        ))


        update_connection.commit()
        update_connection.close()



        item_name_entry.delete(0, END)
        brand_entry.delete(0, END)
        quantity_entry.delete(0, END)
        warehouse_location_entry.delete(0, END)
        create_purches_entry.delete(0, END)
        selling_price_entry.delete(0, END)
        discount_entry.delete(0, END)
        supplier_entry.delete(0, END)
        barcode_entry.delete(0, END)


    def delete_button_function():
        delete_connection = sqlite3.connect('inventoryDB.db')
        delete_cursor = delete_connection.cursor()
        delete_cursor.execute("""
            delete from items
            where barcode = ?
        """, (barcode_entry.get(),))  # Corrected line

        x = items_list.selection()
        for selected in x:
            items_list.delete(selected)

        delete_connection.commit()
        delete_connection.close()





        item_name_entry.delete(0, END)
        brand_entry.delete(0, END)
        quantity_entry.delete(0, END)
        warehouse_location_entry.delete(0, END)
        create_purches_entry.delete(0, END)
        selling_price_entry.delete(0, END)
        discount_entry.delete(0, END)
        supplier_entry.delete(0, END)
        barcode_entry.delete(0, END)











    #   create the select button
    select_record_button = CTkButton(item_toplevel_window, command = select_record)
    # create the Barcode item entry
    barcode_entry = CTkEntry(item_toplevel_window, placeholder_text= 'BarCode Number', width=290, height=40, font=('Arial', 17))
    barcode_entry.grid(column =0, row = 0, padx=30, pady=20)
    # create item name entry
    item_name_entry = CTkEntry(item_toplevel_window, placeholder_text= 'Item Name', width=290, height=40, font=('Arial', 17))
    item_name_entry.grid(column = 1, row = 0, padx=30, pady=20)
    # create brand entry
    brand_entry = CTkEntry(item_toplevel_window, placeholder_text= 'Brand', width=290, height=40, font=('Arial', 17))
    brand_entry.grid(column =2, row = 0, padx=30, pady=20)
    # create material category
    material_optionmenu = CTkOptionMenu(item_toplevel_window, values=clothing_materials, width=290, height=40, font=('Arial', 17))
    material_optionmenu.grid(column =0, row =1, padx=30, pady=20)
    # create quantity entry
    quantity_entry = CTkEntry(item_toplevel_window, placeholder_text= 'Quantity', width=290, height=40, font=('Arial', 17))
    quantity_entry.grid(column =1 , row =1, padx=30, pady=20)
    # create warehouse location entry
    warehouse_location_entry = CTkEntry(item_toplevel_window, placeholder_text= 'Warehouse Name', width=290, height=40, font=('Arial', 17))
    warehouse_location_entry.grid(column = 2, row =1, padx=30, pady=20)
    # create purches price entry
    create_purches_entry = CTkEntry(item_toplevel_window, placeholder_text= 'Purches Price', width=290, height=40, font=('Arial', 17))
    create_purches_entry.grid(column = 0, row =2, padx=30, pady=20)
    # create selling price entry 
    selling_price_entry = CTkEntry(item_toplevel_window, placeholder_text= 'Selling Price', width=290, height=40, font=('Arial', 17))
    selling_price_entry.grid(column = 1, row =2, padx=30, pady=20)
    # create discount entry 
    discount_entry = CTkEntry(item_toplevel_window, placeholder_text= 'Discount', width=290, height=40, font=('Arial', 17))
    discount_entry.grid(column = 2, row =2, padx=30, pady=20)
    # create supplier entry
    supplier_entry = CTkEntry(item_toplevel_window, placeholder_text="Add Supplier", width= 290, height=40 , font=('Arial',17))
    supplier_entry.grid(column = 3, row = 0, padx = 30 , pady = 20)





    ####                CREATE THE BUTTONS [SUBMIT , UPDATE , DELETE]
    item_page_submit_button = CTkButton(item_toplevel_window, text='Submit', height=40, fg_color='#467D35', font=('Arial', 17, 'bold'), command = submit_button_function)
    item_page_submit_button.grid(column = 4, row = 0, padx=30, pady=20)
    ##      UPDATE BUTTON
    item_page_update_button = CTkButton(item_toplevel_window, text='Update', height=40, fg_color='#B59460', font=('Arial', 17, 'bold'), command = update_button_function)
    item_page_update_button.grid(column = 4, row = 1, padx=30, pady=20)
    ##      DELETE BUTTON
    item_page_delete_button = CTkButton(item_toplevel_window, text='Delete', height=40, fg_color= '#723637', font=('Arial', 17, 'bold'), command = delete_button_function)
    item_page_delete_button.grid(column = 4, row = 2, padx=30, pady=20)










    #           CREATE THE DATA BASE TREEVIEW LIST

    #   first i will create the frame
    tree_view_frame = CTkFrame(item_toplevel_window)
    tree_view_frame.place(relwidth =1, y =300, relheight=1)
    #   after creating the frame i create the scroll bar
    scroll_bar  = ttk.Scrollbar(tree_view_frame)
    scroll_bar.pack(side=RIGHT, fill=Y)

    #ADD STYLE
    style = ttk.Style()
    #CONFIGURE THE TREEVIEW COLOR
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight =40 ,font = ("Arial", 10, "bold"))
    style.map("Treeview", background = [("selected" , "#347083")])
    #   now i will create the treeview element

    items_list = ttk.Treeview(tree_view_frame, yscrollcommand=scroll_bar, selectmode='extended',style='Treeview')
    items_list.place(relheight=1, relwidth=1)

    #    HERE IS GIVINE A FUNCTION TO SCROLLBAR
    scroll_bar.config(command = items_list.yview)

    #   HERE IS CREATING THE TREEVIEW COLUMNS
    items_list['columns'] = ('Barcode','ItemName','Brand','Material','Quantity', 'WarehouseName','PurchesPrice','SellingPrice', 'Discount', 'supplier_name')

    items_list.column('#0',width=0 ,stretch=NO)
    items_list.column('Barcode', width=120, anchor=W)
    items_list.column('ItemName', width=120,anchor='center')
    items_list.column('Brand', width=120,anchor='center')
    items_list.column('Material', width=120,anchor='center')
    items_list.column('Quantity',width=120 , anchor='center')
    items_list.column('WarehouseName', width=120,anchor='center')
    items_list.column('PurchesPrice', width=120,anchor='center')
    items_list.column('SellingPrice', width=120,anchor='center')
    items_list.column('Discount', width=120,anchor='center')
    items_list.column('supplier_name', width=120,anchor='center')


    items_list.column('#0', anchor=W)
    items_list.heading('Barcode', text='Barcode', anchor=W)
    items_list.heading('ItemName', text='ItemName', anchor='center')
    items_list.heading('Brand', text='Brand', anchor='center')
    items_list.heading('Material', text='Material', anchor='center')
    items_list.heading('Quantity', text='Quantity', anchor='center')
    items_list.heading('WarehouseName', text='WarehouseName', anchor='center')
    items_list.heading('PurchesPrice', text='PurchesPrice', anchor='center')
    items_list.heading('SellingPrice', text='SellingPrice', anchor='center')
    items_list.heading('Discount', text='Discount', anchor='center')
    items_list.heading('supplier_name', text='supplier_name', anchor='center')



    items_list.bind('<ButtonRelease-1>',select_record)


    database_query()
    
    item_toplevel_window.mainloop()




def returns_window():
    returns_toplevel_window = CTkToplevel()
    returns_toplevel_window.title('Items')
    returns_toplevel_window.geometry('900x900')
    set_appearance_mode('System')







    #create the barcode entery
    barcode_returns = CTkEntry(returns_toplevel_window, placeholder_text='BarCode', height=40, width=290, font=('Arial', 17))
    barcode_returns.grid(column =0, row = 0, padx=30, pady=20)
    # create the Barcode item entry
    client_name_return_entry = CTkEntry(returns_toplevel_window, placeholder_text= 'Client Name', width=290, height=40, font=('Arial', 17))
    client_name_return_entry.grid(column =1, row = 0, padx=30, pady=20)
    # create item name entry
    client_phone_number_return_entry = CTkEntry(returns_toplevel_window, placeholder_text= 'Phone Number', width=290, height=40, font=('Arial', 17))
    client_phone_number_return_entry.grid(column = 2, row = 0, padx=30, pady=20)
    # create brand entry
    items_return_entry = CTkTextbox(returns_toplevel_window, width=290, height=90, font=('Arial', 17))
    items_return_entry.grid(column =0, row = 1, padx=30, pady=20)







    ####                CREATE THE BUTTONS [SUBMIT , UPDATE , DELETE]
    return_page_submit_button = CTkButton(returns_toplevel_window, text='Submit', height=40, fg_color='#467D35', font=('Arial', 17, 'bold'))
    return_page_submit_button.grid(column = 3, row = 0, padx=30, pady=20)
    ##      UPDATE BUTTON
    return_page_update_button = CTkButton(returns_toplevel_window, text='Update', height=40, fg_color='#B59460', font=('Arial', 17, 'bold'))
    return_page_update_button.grid(column = 3, row = 1, padx=30, pady=20)
    ##      DELETE BUTTON
    return_page_delete_button = CTkButton(returns_toplevel_window, text='Delete', height=40, fg_color= '#723637', font=('Arial', 17, 'bold'))
    return_page_delete_button.grid(column = 4, row = 0, padx=30, pady=20)











    #           CREATE THE DATA BASE TREEVIEW LIST

    #   first i will create the frame
    tree_view_frame = CTkFrame(returns_toplevel_window)
    tree_view_frame.place(relwidth =1, y =200, relheight=1)
    #   after creating the frame i create the scroll bar
    scroll_bar  = ttk.Scrollbar(tree_view_frame)
    scroll_bar.pack(side=RIGHT, fill=Y)

    #ADD STYLE
    style = ttk.Style()
    #CONFIGURE THE TREEVIEW COLOR
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight =40 ,font = ("Arial", 10, "bold"))
    style.map("Treeview", background = [("selected" , "#347083")])
    #   now i will create the treeview element

    return_list = ttk.Treeview(tree_view_frame, yscrollcommand=scroll_bar, selectmode='extended',style='Treeview')
    return_list.place(relheight=1, relwidth=1)

    #    HERE IS GIVINE A FUNCTION TO SCROLLBAR
    scroll_bar.config(command = sales_list.yview)

    #   HERE IS CREATING THE TREEVIEW COLUMNS
    return_list['columns'] = ('Barcode','ClientName','PhoneNumber','Items')

    return_list.column('#0',width=0 ,stretch=NO)
    return_list.column('Barcode', width=120, anchor=W)
    return_list.column('ClientName', width=120,anchor='center')
    return_list.column('PhoneNumber', width=120,anchor='center')
    return_list.column('Items', width=120,anchor='center')



    return_list.column('#0', anchor=W)
    return_list.heading('Barcode', text='Barcode', anchor=W)
    return_list.heading('ClientName', text='ClientName', anchor='center')
    return_list.heading('PhoneNumber', text='PhoneNumber', anchor='center')
    return_list.heading('Items', text='Items', anchor='center')


    returns_toplevel_window.mainloop()












def cliens_window():
    client_toplevel_window = CTkToplevel()
    client_toplevel_window.title('Items')
    client_toplevel_window.geometry('900x900')
    set_appearance_mode('System')




    # create the Barcode item entry
    client_name_entry = CTkEntry(client_toplevel_window, placeholder_text= 'Client Name', width=290, height=40, font=('Arial', 17))
    client_name_entry.grid(column =0, row = 0, padx=30, pady=20)
    # create item name entry
    client_phone_number_entry = CTkEntry(client_toplevel_window, placeholder_text= 'Phone Number', width=290, height=40, font=('Arial', 17))
    client_phone_number_entry.grid(column = 1, row = 0, padx=30, pady=20)
    # create brand entry
    items_entry = CTkTextbox(client_toplevel_window, width=290, height=90, font=('Arial', 17))
    items_entry.grid(column =2, row = 0, padx=30, pady=20)







    ####                CREATE THE BUTTONS [SUBMIT , UPDATE , DELETE]
    client_page_submit_button = CTkButton(client_toplevel_window, text='Submit', height=40, fg_color='#467D35', font=('Arial', 17, 'bold'))
    client_page_submit_button.grid(column = 3, row = 0, padx=30, pady=20)
    ##      UPDATE BUTTON
    client_page_update_button = CTkButton(client_toplevel_window, text='Update', height=40, fg_color='#B59460', font=('Arial', 17, 'bold'))
    client_page_update_button.grid(column = 3, row = 1, padx=30, pady=20)
    ##      DELETE BUTTON
    client_page_delete_button = CTkButton(client_toplevel_window, text='Delete', height=40, fg_color= '#723637', font=('Arial', 17, 'bold'))
    client_page_delete_button.grid(column = 4, row = 0, padx=30, pady=20)











    #           CREATE THE DATA BASE TREEVIEW LIST

    #   first i will create the frame
    tree_view_frame = CTkFrame(client_toplevel_window)
    tree_view_frame.place(relwidth =1, y =200, relheight=1)
    #   after creating the frame i create the scroll bar
    scroll_bar  = ttk.Scrollbar(tree_view_frame)
    scroll_bar.pack(side=RIGHT, fill=Y)

    #ADD STYLE
    style = ttk.Style()
    #CONFIGURE THE TREEVIEW COLOR
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight =40 ,font = ("Arial", 10, "bold"))
    style.map("Treeview", background = [("selected" , "#347083")])
    #   now i will create the treeview element

    client_list = ttk.Treeview(tree_view_frame, yscrollcommand=scroll_bar, selectmode='extended',style='Treeview')
    client_list.place(relheight=1, relwidth=1)

    #    HERE IS GIVINE A FUNCTION TO SCROLLBAR
    scroll_bar.config(command = client_list.yview)

    #   HERE IS CREATING THE TREEVIEW COLUMNS
    sales_list['columns'] = ('ClientID','ClientName','PhoneNumber','Items')

    client_list.column('#0',width=0 ,stretch=NO)
    client_list.column('ClientID', width=120, anchor=W)
    client_list.column('ClientName', width=120,anchor='center')
    client_list.column('PhoneNumber', width=120,anchor='center')
    client_list.column('Items', width=120,anchor='center')



    client_list.column('#0', anchor=W)
    client_list.heading('ClientID', text='ClientID', anchor=W)
    client_list.heading('ClientName', text='ClientName', anchor='center')
    client_list.heading('PhoneNumber', text='PhoneNumber', anchor='center')
    client_list.heading('Items', text='Items', anchor='center')


    client_toplevel_window.mainloop()














def suppliers_window():
    supplier_toplevel_window = CTkToplevel()
    supplier_toplevel_window.title('Items')
    supplier_toplevel_window.geometry('900x900')
    set_appearance_mode('System')

    # create the supplier name entry
    supplier_name_entry = CTkEntry(supplier_toplevel_window, placeholder_text= 'Name', width=290, height=40, font=('Arial', 17))
    supplier_name_entry.grid(column =0, row = 0, padx=30, pady=20)
    # create supplier phone number
    phone_number_entry = CTkEntry(supplier_toplevel_window, placeholder_text= 'Phone Number', width=290, height=40, font=('Arial', 17))
    phone_number_entry.grid(column = 1, row = 0, padx=30, pady=20)
    # create goods entry
    goods_entry = CTkTextbox(supplier_toplevel_window, width=290, height=90, font=('Arial', 17))
    goods_entry.grid(column =2, row = 0, padx=30, pady=20)
    # create reciece date entry
    recieve_date_entry = CTkEntry(supplier_toplevel_window, placeholder_text= 'Recieve Date', width=290, height=40, font=('Arial', 17))
    recieve_date_entry.grid(column = 0, row =1, padx=30, pady=20)


    ####                CREATE THE BUTTONS [SUBMIT , UPDATE , DELETE]
    supplier_page_submit_button = CTkButton(supplier_toplevel_window, text='Submit', height=40, fg_color='#467D35', font=('Arial', 17, 'bold'))
    supplier_page_submit_button.grid(column = 3, row = 0, padx=30, pady=20)
    ##      UPDATE BUTTON
    supplier_page_update_button = CTkButton(supplier_toplevel_window, text='Update', height=40, fg_color='#B59460', font=('Arial', 17, 'bold'))
    supplier_page_update_button.grid(column = 3, row = 1, padx=30, pady=20)
    ##      DELETE BUTTON
    supplier_page_delete_button = CTkButton(supplier_toplevel_window, text='Delete', height=40, fg_color= '#723637', font=('Arial', 17, 'bold'))
    supplier_page_delete_button.grid(column = 4, row = 0, padx=30, pady=20)











    #           CREATE THE DATA BASE TREEVIEW LIST

    #   first i will create the frame
    tree_view_frame = CTkFrame(supplier_toplevel_window)
    tree_view_frame.place(relwidth =1, y =200, relheight=1)
    #   after creating the frame i create the scroll bar
    scroll_bar  = ttk.Scrollbar(tree_view_frame)
    scroll_bar.pack(side=RIGHT, fill=Y)

    #ADD STYLE
    style = ttk.Style()
    #CONFIGURE THE TREEVIEW COLOR
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight =40 ,font = ("Arial", 10, "bold"))
    style.map("Treeview", background = [("selected" , "#347083")])
    #   now i will create the treeview element

    supplier_list = ttk.Treeview(tree_view_frame, yscrollcommand=scroll_bar, selectmode='extended',style='Treeview')
    sales_list.place(relheight=1, relwidth=1)

    #    HERE IS GIVINE A FUNCTION TO SCROLLBAR
    scroll_bar.config(command = supplier_list.yview)

    #   HERE IS CREATING THE TREEVIEW COLUMNS
    supplier_list['columns'] = ('SupplierID', 'SupplierName', 'Goods', 'PhoneNumber', 'RecieptDate')

    supplier_list.column('#0',width=0 ,stretch=NO)
    supplier_list.column('SupplierID', width=120, anchor=W)
    supplier_list.column('SupplierName', width=120,anchor='center')
    supplier_list.column('Goods', width=120,anchor='center')
    supplier_list.column('PhoneNumber', width=120,anchor='center')
    supplier_list.column('RecieptDate',width=120 , anchor='center')



    supplier_list.column('#0', anchor=W)
    supplier_list.heading('SupplierID', text='SupplierID', anchor=W)
    supplier_list.heading('SupplierName', text='SupplierName', anchor='center')
    supplier_list.heading('Goods', text='Goods', anchor='center')
    supplier_list.heading('PhoneNumber', text='PhoneNumber', anchor='center')
    supplier_list.heading('RecieptDate', text='RecieptDate', anchor='center')
    supplier_toplevel_window.mainloop()


def sales_graph_window():
    pass
def sales_list_window():
    pass








#                                                   END FUNCTIONS CONTAINER









#################################################################################################################################################################################################
#################################################################################################################################################################################################
#################################################################################################################################################################################################

# 01 creating barcode entry
barcode_entry = CTkEntry(window, placeholder_text= 'BarCode Number', width=290, height=40, font=('Arial', 17))
barcode_entry.grid(padx =30, pady =20)

# 02 creating client name entry
client_name_entry = CTkEntry(window, placeholder_text= 'client name', width=290, height=40, font=('Arial', 17))
client_name_entry.grid(column = 1, row = 0)

# 03 creatind client phonenumber entry
client_phonenumber_entry = CTkEntry(window, placeholder_text= 'client phonenumber', width=290, height=40, font=('Arial', 17))
client_phonenumber_entry.grid(column = 0, row = 1)

# 05 creating total price entry with tax
total_price_entry = CTkEntry(window, placeholder_text= 'total price', width=290, height=40, font=('Arial', 17))
total_price_entry.grid(column = 1, row = 1)

# 06 create the recite number entry auto increment
paid_entry = CTkEntry(window, placeholder_text= 'Paid', width=290, height=40, font=('Arial', 17))
paid_entry.grid(pady = 20)

# 06 create the recite number entry auto increment
discount_entry = CTkEntry(window, placeholder_text= 'Discount', width=290, height=40, font=('Arial', 17))
discount_entry.grid(pady = 20, column = 1, row =2 )
# 07 create the quantity entry to write the quantity was sold
quantity_entry = CTkEntry(window, placeholder_text = 'Quantity', width= 290 , height=40 , font=("Arial", 17))
quantity_entry.grid(column = 2, row = 2, padx = 30)










#################################################################################################################################################################################################
#################################################################################################################################################################################################
#################################################################################################################################################################################################
#                                                                   HERE I WILL WRITE THE FUNCTION OF SALES PAGE
"""
                #   THE EXPLAINING TO THE FUNCTIONALITY   #
[1]     make the submit button insert the data from the entries to sales list in the landing page
            [+]     get all values from the entries
            [+]     insert the values to the list
            [+]     create the connection to the item table to search the item by barcode
            [+]     create fetch all to the database
            [+]     insert all values by for loop
            [+]     create the connection to the database
            [+]     minus the quantity from the item in the item table
[2]     create the select button. if i select the row of data, it will insert the column data in the entries
[3]     the update button it will update the row was selected
            [+]     create the select button function
            [+]     insert all values
            [+]     update by list update function
[4]     the delete button functionality it you in the first should select the row and click on the delete button it will delete it
            [+]     use delete function to the list with out sqlite connection
[5]     sale button it save the rows in the report window and add new client in the client page
            [+]     create the database connection with sales table
            [+]     make the insert into < sales table > values() .... sql code
            [+]     insert the rows with the same client name and number
[6]     the print button it print the sales list to the client
"""
#       THE FUNCTION OF SUBMIT BUTTON
def submit_button_sales():

    searching = barcode_entry.get()
    sale_connection = sqlite3.connect('inventoryDB.db')
    sale_cursor = sale_connection.cursor()

    sale_cursor.execute("""
            SELECT * FROM items WHERE barcode LIKE ?
    """, (f'%{searching.strip()}%',))
    records  = sale_cursor.fetchall()

    for record in records:
        sales_list.insert(parent='', text='',index='end', values=(record[1] , client_name_entry.get() , client_phonenumber_entry.get() ,record[8] , quantity_entry.get(),discount_entry.get(),paid_entry.get(),total_price_entry.get() ))
    sale_connection.commit()
    sale_connection.close()










def select_record(e):
        barcode_entry.delete(0, END)
        client_name_entry.delete(0, END)
        client_phonenumber_entry.delete(0, END)
        total_price_entry.delete(0, END)
        paid_entry.delete(0, END)
        discount_entry.delete(0, END)
        quantity_entry.delete(0, END)
        

        select = sales_list.focus()
        values = sales_list.item(select,'values')

        barcode_entry.insert(0,values[0])
        client_name_entry.insert(0,values[1])
        client_phonenumber_entry.insert(0,values[2])
        total_price_entry.insert(0,values[7])
        paid_entry.insert(0, values[6])
        discount_entry.insert(0, values[5])
        quantity_entry.insert(0, values[4])




          
    #  THE FUNCTION OF UPDATE BUTTON
def update_button_sales():
    # this function to update the row is selected and insert it in the fields
    select = sales_list.focus()  # الحصول على العنصر المحدد
    barcode_value = barcode_entry.get()
    # **🔄 تحديث العنصر في Treeview مباشرة**
    sales_list.item(select, values=(
        barcode_entry.get(),
        client_name_entry.get(),
        client_phonenumber_entry.get(),
        total_price_entry.get(),
        paid_entry.get(),
        discount_entry.get(),
        quantity_entry.get(),
    ))



    barcode_entry.delete(0, END)
    client_name_entry.delete(0, END)
    client_phonenumber_entry.delete(0, END)
    total_price_entry.delete(0, END)
    paid_entry.delete(0, END)
    discount_entry.delete(0, END)
    quantity_entry.delete(0, END)
  





#       THE FUNCTION OF DELTE BUTTON
def delete_button_sales():
    x = sales_list.selection()
    for selected in x:
        sales_list.delete(selected)





#       THE FUNCTION TO PRINT THE RECEIPT
def print_records_button():
    # [1] get all rows from sales_list and add it to sales db inventoryDB.db the list in the sales report list page
    rows = []
    for row in sales_list.get_children():
        rows.append(sales_list.item(row)['values'])
    # [2] create the connection to the database
    sales_connection = sqlite3.connect('inventoryDB.db')
    sales_cursor = sales_connection.cursor()
    # [3] insert the values to the sales table
    for row in rows:
        sales_cursor.execute("""
            INSERT INTO sales (barcode, client_name, phone_number, total_price, paid, discount, quantity)
            VALUES (?,?,?,?,?,?,?)
        """, (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    sales_connection.commit()
    sales_connection.close()
    # [4] delete all rows from the sales list
    x = sales_list.selection()
    for selected in x:
        sales_list.delete(selected)
    







#                                                                   THE END OF FUNCTION OF BUTTON CONTAINER
#################################################################################################################################################################################################
#################################################################################################################################################################################################
#################################################################################################################################################################################################
#here creating three button [submit , update ,delete, print the recipte]
#   create the select button
select_record_button = CTkButton(window, command = select_record)
#create the submit button 
submit_button = CTkButton(window , height=40 , text='Submit' , fg_color='#467D35', font=('Arial', 17, 'bold'), command= submit_button_sales)
submit_button.grid(column = 2 , row = 0 , padx =30)
#create the update button
update_button = CTkButton(window, text='Update', height=40 , fg_color='#B59460', font=('Arial', 17, 'bold'), command= update_button_sales)
update_button.grid(column = 2, row = 1 , padx =30)
#create the delete button
delete_button = CTkButton(window,text='Delete',height=40, fg_color= '#723637', font=('Arial', 17, 'bold'), command= delete_button_sales)
delete_button.grid(column = 3 , row = 0, padx =30)
#create the print button
print_button = CTkButton(window , text="Print & Sale", height=40, fg_color='#5D4A95', font=('Arial', 17, 'bold'), command= print_records_button)
print_button.grid(column = 3 , row = 1, padx =30)
#creating daily report button to open new window
daily_report_button = CTkButton(window, text='Daily Report', command=open_daily_report_window, height=40, font=('Arial', 17, 'bold'))
daily_report_button.grid(column =4 , row = 0, padx=30)
#creating inventory open new window
inventory_container = CTkButton(window, text = 'Inventory', height = 40 , command = inventory_open_window, font=('Arial', 17, 'bold'))
inventory_container.grid(column = 4 , row =1 , padx = 30)






"""
create the menu bar called More Options .
the menu bar content is will help the user to manage there shop or inventory well.
i will make a to menu bar option
second one to graph and reports 
first one content
[
add item,
returns,
clients,
suppliers,
]
second one
[
sales graph,
sales list
]
"""

# start menu bar container
menu = Menu(window)
window.config(menu=menu)
more_options = Menu(menu)
menu.add_cascade(label='More Options', menu=more_options)
# first menu bar option
more_options.add_command(label='Items', command=items_window)
#second menu bar option
more_options.add_command(label='Returns', command=returns_window)
#third menu bar option
more_options.add_command(label='Clients', command= cliens_window)
#fourth menu bar option
more_options.add_command(label='Suppliers', command= suppliers_window)

# start second menu bar option
graph_reports = Menu(menu)
menu.add_cascade(label='Graphs and Reports', menu=graph_reports)
# first menu bar option
graph_reports.add_command(label='Sales Graph', command=sales_graph_window)
#second menu bar option
graph_reports.add_command(label='Sales List', command=sales_list_window)

# end menu bar container

#           CREATE THE DATA BASE TREEVIEW LIST

#   first i will create the frame
tree_view_frame = CTkFrame(window)
tree_view_frame.place(relwidth =1, y =200, relheight=1)
#   after creating the frame i create the scroll bar
scroll_bar  = ttk.Scrollbar(tree_view_frame)
scroll_bar.pack(side=RIGHT, fill=Y)

#ADD STYLE
style = ttk.Style()
#CONFIGURE THE TREEVIEW COLOR
style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight =40 ,font = ("Arial", 10, "bold"))
style.map("Treeview", background = [("selected" , "#347083")])
#   now i will create the treeview element

sales_list = ttk.Treeview(tree_view_frame, yscrollcommand=scroll_bar, selectmode='extended',style='Treeview')
sales_list.place(relheight=1, relwidth=1)

#    HERE IS GIVINE A FUNCTION TO SCROLLBAR
scroll_bar.config(command = sales_list.yview)

#   HERE IS CREATING THE TREEVIEW COLUMNS
sales_list['columns'] = ('Barcode','ClientName','PhoneNumber','SellingPrice','Quantity', 'Discount','Paid','TotalPrice')

sales_list.column('#0',width=0 ,stretch=NO)
sales_list.column('Barcode', width=120, anchor=W)
sales_list.column('ClientName', width=120,anchor='center')
sales_list.column('PhoneNumber', width=120,anchor='center')
sales_list.column('SellingPrice', width=120,anchor='center')
sales_list.column('Quantity',width=120 , anchor='center')
sales_list.column('Discount', width=120,anchor='center')
sales_list.column('Paid', width=120,anchor='center')
sales_list.column('TotalPrice', width=120,anchor='center')


sales_list.column('#0', anchor=W)
sales_list.heading('Barcode', text='Barcode', anchor=W)
sales_list.heading('ClientName', text='ClientName', anchor='center')
sales_list.heading('PhoneNumber', text='PhoneNumber', anchor='center')
sales_list.heading('SellingPrice', text='SellingPrice', anchor='center')
sales_list.heading('Quantity', text='Quantity', anchor='center')
sales_list.heading('Discount', text='Discount', anchor='center')
sales_list.heading('Paid', text='Paid', anchor='center')
sales_list.heading('TotalPrice', text='TotalPrice', anchor='center')







sales_list.bind('<ButtonRelease-1>',select_record)
window.mainloop()