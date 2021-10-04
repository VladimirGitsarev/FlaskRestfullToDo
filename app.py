from datetime import datetime

from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app'
db = SQLAlchemy(app)
mm = Marshmallow(app)
api = Api(app)


if __name__ == '__main__':
    app.run(debug=True)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))
    done = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'Item {self.name} - {self.date}'


class ItemListResource(Resource):
    def get(self):
        items = Item.query.all()
        return items_schema.dump(items)

    def post(self):
        new_item = Item(
            name=request.json['name'],
            description=request.json['description']
        )
        db.session.add(new_item)
        db.session.commit()
        return item_schema.dump(new_item)


class ItemResource(Resource):
    def get(self, item_id):
        post = Item.query.get_or_404(item_id)
        return item_schema.dump(post)

    def patch(self, item_id):
        item = Item.query.get_or_404(item_id)

        item.name = request.json.get('name', item.name)
        item.description = request.json.get('description', item.description)
        item.done = request.json.get('done', item.done)
        db.session.commit()
        return item_schema.dump(item)

    def delete(self, item_id):
        post = Item.query.get_or_404(item_id)
        db.session.delete(post)
        db.session.commit()
        return '', 204


class ItemSchema(mm.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'done', 'date')
        model = Item


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
api.add_resource(ItemListResource, '/items')
api.add_resource(ItemResource, '/items/<int:item_id>')

