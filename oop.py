import os
import tkinter as tk
from tkinter import messagebox

# وظيفة لحفظ الفاتورة في ملف TXT
def save_invoice():
    customer_name = name_entry.get()
    items = items_text.get("1.0", tk.END).strip()
    total_price = total_entry.get()

    if not customer_name or not items or not total_price:
        messagebox.showerror("خطأ", "يرجى ملء جميع الحقول!")
        return

    invoice_text = f"فاتورة المبيعات\n\nاسم العميل: {customer_name}\n\nالعناصر:\n{items}\n\nالإجمالي: {total_price} جنيه\n"
    
    with open("invoice.txt", "w", encoding="utf-8") as file:
        file.write(invoice_text)

    messagebox.showinfo("نجاح", "تم حفظ الفاتورة بنجاح!")

# وظيفة لطباعة الفاتورة من ملف TXT
def print_invoice():
    save_invoice()  # حفظ الفاتورة قبل الطباعة
    try:
        os.startfile("invoice.txt", "print")  # طباعة الفاتورة
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ أثناء الطباعة: {e}")

# واجهة المستخدم
root = tk.Tk()
root.title("إنشاء فاتورة")

tk.Label(root, text="اسم العميل:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="العناصر:").grid(row=1, column=0)
items_text = tk.Text(root, height=5, width=30)
items_text.grid(row=1, column=1)

tk.Label(root, text="الإجمالي (جنيه):").grid(row=2, column=0)
total_entry = tk.Entry(root)
total_entry.grid(row=2, column=1)

save_button = tk.Button(root, text="حفظ الفاتورة", command=save_invoice)
save_button.grid(row=3, column=0, pady=10)

print_button = tk.Button(root, text="طباعة الفاتورة", command=print_invoice)
print_button.grid(row=3, column=1, pady=10)

root.mainloop()
