from app import db

class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    numb=db.Column(db.Integer)
    typename=db.Column(db.String)
    itemname=db.Column(db.String)
    size_i=db.Column(db.Integer)
    price=db.Column(db.Integer)
    day=db.Column(db.Date)
    #isold=db.Column(db.Boolean)

    def __repr__(self):
        return '<Item {} {} size= {} price= {}>'.format(self.typename,self.itemname,self.size_i,self.price)

