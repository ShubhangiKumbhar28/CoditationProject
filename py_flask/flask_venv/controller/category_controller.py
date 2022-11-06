from app import app
from flask import Blueprint
from model.category_add import category_add
from flask import request
obj =category_add()

@app.route("/category/get")
def category_get_controller():
    return obj.category_get_model()

@app.route("/category/addone", methods=["POST"])
def category_addone_controller():
    return obj.category_addone_model(request.form)

@app.route("/category/update", methods=["PUT"])
def category_update_controller():
    return obj.categoryt_update_model(request.form)

@app.route("/category/delete/<category_id>", methods=["DELETE"])
def category_delete_controller(category_id):
    return obj.category_delete_model(category_id)