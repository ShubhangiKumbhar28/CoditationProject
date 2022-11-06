from flask import Blueprint
from app import app
from model.product_add import product_add
from flask import render_template
obj =product_add()



@app.route("/product/get")
def product_get_controller():
    return obj.product_get_model()

@app.route("/product/addone", methods=["POST"])
def product_addone_controller():
    return obj.product_addone_model(request.form)

@app.route("/product/update", methods=["PUT"])
def product_update_controller():
    return obj.product_update_model(request.form)

@app.route("/product/delete/<productid>", methods=["DELETE"])
def product_delete_controller(productid):
    return obj.product_delete_model(productid)