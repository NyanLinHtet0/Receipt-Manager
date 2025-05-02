from Menu.menu import menu
from Code.R_manager import R_manager

def option2(R_manager:R_manager):
    hub_menu = ['View Receipts','Add Receipt']
    view_menu = ['View Selected Receipt']
    r_savepath = './data/saves/r_saves'
    while True:
        x = menu(hub_menu)
        if x == len(hub_menu):
            break
        #exit case
        elif x == 1:#view receipt
            R_manager.view_receipts()
            while True:
                try:
                    num = int(input("Enter receipt by number to view the receipt: "))
                    break  # If input is successfully converted to int, break out of the loop
                except ValueError:
                    print("Please enter a valid integer.")
            R_manager.import_receipt(num-1)
        elif x == 2:#add receipt
            receipt = R_manager.make_receipt()
            save = input("Would you like to save the Receipt? (Y/N)\n")
            if save == 'Y' or save =='y':
                R_manager.savereceipt(receipt)
            else:
                receipt = None
            
# import tkinter as tk
# from tkinter import simpledialog, messagebox

# def option2(R_manager):
#     # Function to handle adding a receipt
#     def add_receipt():
#         receipt = R_manager.make_receipt()
#         save = messagebox.askyesno("Save Receipt", "Would you like to save the Receipt?")
#         if save:
#             R_manager.savereceipt(receipt)
    
#     # Function to handle viewing receipts
#     def view_receipts():
#         receipt_list = R_manager.view_receipts()

#         selected_receipt = simpledialog.askinteger("View Receipts", "Enter the receipt number to view:")
#         if selected_receipt is not None:
#             receipt_info = receipt_list[selected_receipt - 1]  # Adjusting index to match user's selection
#             messagebox.showinfo("View Receipt", receipt_info)

#     # Create the main window
#     root = tk.Tk()
#     root.title("Receipts Menu")
#     root.geometry("1000x1000")

#     # Function to handle button clicks
#     def handle_click(option):
#         if option == "Add Receipt":
#             add_receipt()
#         elif option == "View Receipts":
#             view_receipts()
#         root.quit()

#     # Create buttons for options
#     add_button = tk.Button(root, text="Add Receipt", command=lambda: handle_click("Add Receipt"))
#     add_button.pack(pady=10)
#     view_button = tk.Button(root, text="View Receipts", command=lambda: handle_click("View Receipts"))
#     view_button.pack(pady=10)

#     root.mainloop()

            


