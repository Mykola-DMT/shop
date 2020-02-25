from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,SelectMultipleField,BooleanField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    numb=IntegerField(u'Number',validators=[DataRequired()])
    typename=StringField(u'Typename',validators=[DataRequired()])
    itemname=StringField(u'Itemname',validators=[DataRequired()])
    #sizes=SelectMultipleField('Selectsize',choices=[('36'),('38'),('40'),('42'),('44'),('46'),('48'),('50'),('52')], coerce=int,option_widget=None)
    size_i=IntegerField(u'Size',validators=[DataRequired()])
    price=IntegerField(u'Price',validators=[DataRequired()])
    # day=DateTimeField('Date')
    # isold=BooleanField('Sold')
    submit=SubmitField('Add')
