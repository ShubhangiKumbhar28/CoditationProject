
from flask import Blueprint
import mysql.connector
import json

class category_add():
    def __init__(self):
        try:
            self.conn=mysql.connector.connect( host="localhost", username="root", password="shu2728", database="category_product_db")
            self.conn.autocommit=True
            self.cur=self.conn.cursor(dictionary=True)
            print("connection successful")
        except:
            print("some error")
    
    def category_get_model(self):
        self.cur.execute("SELECT * FROM category")
        result=self.cur.fetchall()
        if (len(result)>0):
            return json.dumps(result)
        else:
            return "No Data Found"
    
    def category_addone_model(self, data):
        self.cur.execute(f"INSERT INTO category(category_name,parent_cat_id,has_child)   values ('{data['category_name']}','{data['parent_cat_id']}','{data['has_child']}')")
       
        return "category  Added successfully."

    def categoryt_update_model(self,data):
        self.cur.execute(f"update category SET category_name='{data['category_name']}' , parent_cat_id='{data['parent_cat_id']}' , has_child='{data['has_child']}'  WHERE category_id={data['category_id']}")
        if self.cur.rowcount>0:
            return "category Updated Cuccessfully"
        else:
            return "Nothing to Update"

    def category_delete_model(self,category_id):
        self.cur.execute(f"DELETE FROM category WHERE category_id={category_id}")
        if self.cur.rowcount>0:
            return "category Deleted Successfully"
        else:
            return "Nothing to Delete "
         
