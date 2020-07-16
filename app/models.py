from app import db


class Country(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_code = db.Column(db.String(4), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    country_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Country({self.country_code}, {self.country_name})'

    def __str__(self):
        return f'({self.country_code}, {self.country_name})'


class Covid19HistoricalData(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_reported = db.Column(db.DATETIME, nullable=False)
    day_number = db.Column(db.SMALLINT, nullable=False)
    month_number = db.Column(db.SMALLINT, nullable=False)
    year_number = db.Column(db.SMALLINT, nullable=False)
    cases = db.Column(db.INTEGER, nullable=True)
    deaths = db.Column(db.INTEGER, nullable=True)
    country_name = db.Column(db.String(100), nullable=False)
    country_code = db.Column(db.String(4), nullable=True)
    country_terr_code = db.Column(db.String(4), nullable=True)
    populationData2019 = db.Column(db.INTEGER, nullable=True)
    continent = db.Column(db.String(40), nullable=False)
    cum_num_14_days_cases_per_100K = db.Column(db.FLOAT, nullable=True)

    def __repr__(self):
        return f'Country({self.date_reported}, {self.country_code}' \
               f', {self.country_name}, {self.cases}, {self.deaths}' \
               f', {self.day_number}, {self.month_number}, {self.year_number}' \
               f', {self.populationData2019}, {self.continent}, {self.cum_num_14_days_cases_per_100K})'

    def __str__(self):
        return f'({self.date_reported}, {self.country_code}, {self.country_name}, {self.cases}, {self.deaths})'
