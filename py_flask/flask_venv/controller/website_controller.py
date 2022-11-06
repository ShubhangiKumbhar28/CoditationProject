# from app import app
# from flask import request
# import mysql.connector
# import json
# from flask import render_template

# conn=mysql.connector.connect( host="localhost", username="root", password="shu2728", database="category_product_db")


# @app.route("/product",methods=['GET','POST'])
# def product_page():
#     if(request.method=='POST'):
#         productname=request.form.get('productname')
#         price=request.form.get('price')
#         decription=request.form.get('decription')
#         product_cat=request.form.get('product_cat')
#         return render_template ('product.html')

# @app.route("/category")
# def category_page():
#     return "This is category page"

