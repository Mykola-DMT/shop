# -*- coding: utf-8 -*-
from app import app
from flask import render_template,flash, redirect, request
from app.forms import AddForm
from datetime import date,datetime
from app.db_setup import init_db, db_session
from app.models import Item
from app import db
from app.tables import Result

@app.route('/')
@app.route('/index')
def index():
    today = {'datetoday':date.today()}
    return render_template('index.html',today=today)

@app.route('/additems', methods=['GET','POST'])
def additems():
    form = AddForm()
    if request.method == 'POST' and form.validate():
        #save item:
        item = Item()
        save_changes(item, form, new=True)
        flash('Item added successfully')
        flash(form.validate())
        return redirect('/index')
    return render_template('additems.html', form=form)

def save_changes(item,form, new=False):
    item.typename=form.typename.data
    item.itemname=form.itemname.data
    item.size_i=form.size_i.data
    item.price=form.price.data
    item.day=date.today()
    item.numb=form.numb.data
    #item.isold=False

    if new:
        db.session.add(item)

    db.session.commit()

def clear_data():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()

@app.route('/showitems', methods=['GET','POST'])
def showitems():
    items=[]
    #items_string=AddForm.data
    qry=db.session.query(Item)
    items=qry.all()
    table = Result(items)
    table.border=True
    totaltoday = 0
    for i in items:
        if i.day == date.today():
            totaltoday+=i.price
    if request.method == 'POST':
        clear_data()
        flash('Cleaned!')
        return redirect('/index')
    return render_template('showitems.html',table=table,totaltoday=totaltoday)

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=8000)


# >>> db.session.delete(me)
# >>> db.session.commit()

    # typename='aaa'
    # itemname='blue'
    # size_i=38
    # price=700
    # db='dataset'
    # con = pymysql.connect(typename=typename,itemname=itemname,size_i=size_i,price=price,db=db, use_unicode=True, charset='utf8')
    # #con = pymysql.connect(use_unicode=True, charset='utf8')
    # cur = con.cursor()
    # cur.execute("SELECT * FROM dataset")
    # data = cur.fetchall()   
    # return render_template("showitems.html", value=data)