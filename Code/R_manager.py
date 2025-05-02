from Code.Receipt import Item, Receipt
from datetime import datetime

class R_manager:
    def __init__(self):
        self.header_file_name = './data/saves/receipt_saves/R_header.txt'
        self.data_file_name = './data/saves/receipt_saves/data/'
        self.receipts_header_info = []
        self.import_header_data()
        self.bubble_sort()

    def get_headers(self):
        return self.receipts_header_info
    
    #this function is used for initializing the class to check for existing receipts
    def import_header_data(self):
        with open(self.header_file_name, 'r') as file:
            for line in file:   
                if line.strip() == "":
                    #the line is empty
                    pass
                else:
                    line = line.strip()
                    line = line.split('\31')    
                    date_parsed = line[3].split(" ")
                    date = date_parsed[0].split("-")
                    time = date_parsed[1].split(":")
                    date_time = datetime(year=int(date[0]), month=int(date[1]), day=int(date[2]), hour=int(time[0]), minute=int(time[1]), second=int(time[2]))
                    receipt_date_time = line[0].split('/')
                    receipt_date_time = datetime(year=int(receipt_date_time[2]), month=int(receipt_date_time[0]), day=int(receipt_date_time[1]))
                    line[0] = receipt_date_time
                    line[3] = date_time
                    self.receipts_header_info.append(tuple(line))
            
    #this function previews the receipts saved
    def view_receipts(self):
        for i in range(len(self.receipts_header_info)):
            header = list(self.receipts_header_info[i])
            print(f'{i+1}) {header[0].strftime("%m/%d/%Y")} {header[1]} ${header[2]}')

    #this function RETURNS a receipt read from a file
    def import_receipt(self, index:int):
        file_path = self.get_save_location_str(self.receipts_header_info[index])
        file_name =  f'{self.receipts_header_info[index][1]}-{self.receipts_header_info[index][3].strftime("%Y_%m_%d_%H_%M_%S")}.txt'
        receipt = Receipt()
        receipt.read_from_file(file_path+file_name)
        receipt.printf()

    #this functions RETURNS './data/saves/receipt_saves/data/<YYYY>/<MM>/<DD>/'
    def get_save_location_str(self, header_info:tuple):             
        date = header_info[0].strftime("%m/%d/%Y")                   
        rcpt_date_reversed = date.split('/')
        rcpt_date_reversed = f'{self.data_file_name}{rcpt_date_reversed[2]}/{rcpt_date_reversed[0]}/{rcpt_date_reversed[1]}/'
        return rcpt_date_reversed
    
    #this function saves the  parameter ,receipt, of a file
    def savereceipt(self, receipt: Receipt):
        #make the time of receipt
        receipt.get_date_time()
        #request header info
        header_info = receipt.get_header_info()
        #make address to save file
        rcpt_file_name = self.get_save_location_str(header_info)+receipt.get_file_name()
        #write ALL data to r_saves
        receipt.write_to_file(rcpt_file_name)
        #add the file into the header
        if len(self.receipts_header_info) > 1:
            for i in range(len(self.receipts_header_info)):
                if header_info[0] > self.receipts_header_info[i][0]:
                    self.receipts_header_info.insert(i, header_info)
                    break
                else:
                    self.receipts_header_info.append(header_info)
                    break
        else:
            self.receipts_header_info.append(header_info)
        #append header information to the file
        with open(self.header_file_name, 'a') as file:
            for i in range(len(header_info)):
                if i < len(header_info)-1:
                    if i == 0:
                        file.write(str(header_info[i].strftime("%m/%d/%Y"))+'\31')
                    else:
                        file.write(str(header_info[i])+'\31')
                else:
                    file.write(str(header_info[i])+'\n')
        self.bubble_sort()
                    
    #This function RETURNS a receipt after prompting the user information using input()
    def make_receipt(self):
        r_info = input("Enter Name and Date with space: \n")
        r_info = r_info.split(' ')
        date = r_info[1].split('/')
        date = datetime(year=int(date[2]), month=int(date[0]), day=int(date[1]))
        
        receipt = Receipt(r_info[0], date) 
        while True:
            i_str_in = input("Enter in this format-> Item Price Person1 Person2 Person3\n")
            if i_str_in == "-1":
                break
            i_str_in= i_str_in.split(' ')
            #NEEDS ITEM NAME AND PRICE to store in a receipt, or won't accept
            if len(i_str_in) > 2:
                i_name = i_str_in[0] 
                i_price = i_str_in[1]
            i_people = i_str_in[2:]
            receipt.add(Item(i_name, i_price, i_people))
        return receipt
    #-----------------------DATA SORTING--------------------------------------------------
    def bubble_sort(self):
        swap = True
        while swap:
            swap = False
            for i in range(len(self.receipts_header_info)-1):
                #get two variables and compare
                first = self.receipts_header_info[i]
                second = self.receipts_header_info[i+1]
                temp = None
                #compare dates
                if first[0] < second[0]:
                    swap = True
                    temp = first
                    self.receipts_header_info[i] = self.receipts_header_info[i+1]
                    self.receipts_header_info[i+1] = temp 