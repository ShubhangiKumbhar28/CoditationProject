from flask import render_template

import mysql.connector
import json

class product_add():
    def __init__(self):
        try:
            self.conn=mysql.connector.connect( host="localhost", username="root", password="shu2728", database="category_product_db")
            self.conn.autocommit=True
            self.cur=self.conn.cursor(dictionary=True)
            print("connection successful")
        except:
            print("some error")
    
    def product_get_model(self):
        self.cur.execute("SELECT * FROM product")
        result=self.cur.fetchall()
        if (len(result)>0):
            return json.dumps(result)
        else:
            return "No Data Found"
    
    def product_addone_model(self, data):
        self.cur.execute(f"INSERT INTO product(productname,price,decription,product_cat)   values ('{data['productname']}','{data['price']}','{data['decription']}','{data['product_cat']}')")
       
        return "Product  Added successfully."

    def product_update_model(self,data):
        self.cur.execute(f"update product SET productname='{data['productname']}' , price='{data['price']}' , product_cat='{data['product_cat']}', decription='{data['decription']}'  WHERE productid={data['productid']}")
        if self.cur.rowcount>0:
            return "Product Updated Cuccessfully"
        else:
            return "Nothing to Update"

    def product_delete_model(self,productid):
        self.cur.execute(f"DELETE FROM product WHERE productid={productid}")
        if self.cur.rowcount>0:
            return "Product Deleted Successfully"
        else:
            return "Nothing to Delete "
         
