from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired


def country_select_query():
    from app.models import Country
    return Country.query


def default_select():
    from app.models import Country
    default_country = Country.query.filter_by(country_code="BR").first()
    return default_country


class CountryForm(FlaskForm):
    country_name = QuerySelectField('Country', query_factory=country_select_query
                                    , validators=[DataRequired()], allow_blank=True, blank_text='Select'
                                    , get_pk=lambda a: a.country_code, get_label='country_name'
                                    , default=default_select())

    def __str__(self):
        return f'{self.country_code}, {self.country_name}'

