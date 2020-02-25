from flask_table import Table, Col

class Result(Table):
    id=Col('Id',show=False)
    numb=Col('Number')
    typename=Col('Type')
    itemname=Col('Name')
    size_i=Col('Size')
    price=Col('Price')
    day=Col('Date')
    #isold=Col('Is sold')