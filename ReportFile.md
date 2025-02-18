

# Report File  

### Progress on the Inventory Management System Project  

---

## Completed Tasks  

### What I Have Done  

I created a database file to store items and connected it to the item page. Additionally, I implemented functionality for the buttons on the item page, including **Submit, Update, and Delete**.  

Currently, I am working on the **Sales Page**, where I am trying to implement the **Sale** button to generate a report in a `.txt` file and create a list of sold items.  

The **Sales Report Page** will include details of the client who purchased the item, the item name, the buyer’s information, and the time of purchase. This page will contain fields for **item name, client phone number, client name, and item barcode**.  

---

## **18/02/2050**  

### **Tasks Completed**  

✅ **Created button functionalities**  
✅ **Connected the buttons to the Sales Report Page**  
✅ **Generated a daily report file**  

---

## **Sales Page & Sales Report Page**  

- The **Sales Page** acts as the landing page since it is the first page the user sees upon opening the application.  
- The **Sales Report Page** displays the list of sales and the daily report of sold items.  

### **Features & Buttons**  

- **Submit** → Adds the item to the sales list.  
- **Sale** → Finalizes the sale and records it in the sales report with client details (name, phone number, and barcode).  
- **Update** → Updates the selected item in the list.  
- **Delete** → Removes the selected item from the list.  
- **Print** → Generates a receipt for the client, saves the sale to the database, and updates the item quantity in stock.  
- **Inventory** → Opens a new window displaying the available inventory.  
- **Sales Report** → Shows the list of sold items.  

---

## **Progress Log**  

### **12:42 PM**  
✔️ Finished the **Submit** button.  
- Functionality: Allows adding items to a client's purchase list to consolidate all purchased items.  

### **7:00 PM**  
✔️ Completed the **Delete** and **Update** buttons.  
✔️ Implemented their functionalities.  
✔️ Removed the **Sale** button and integrated its functionality into the **Print** button.  

---

## **Print Button Functionality**  

The **Print** button now performs multiple tasks:  
1. Saves the sale to the sales database.  
2. Generates the report and client receipt.  
3. Deducts the sold quantity from the stock inventory.  

---
