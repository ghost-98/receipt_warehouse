from .. import db


class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20))
    total_amount = db.Column(db.String(20))
    text_data = db.Column(db.Text)
    image_path = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Receipt {self.store_name}>'