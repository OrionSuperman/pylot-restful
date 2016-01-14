""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def get_all_products(self):
        query = "SELECT * FROM products"
        result = self.db.query_db(query)
        return result

    def get_product_info(self, id):
        query="SELECT * FROM products WHERE id={}".format(id)
        result = self.db.query_db(query)
        return result

    def create_product(self, info):
        query = "INSERT INTO products (name, description, price, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(info['name'], info['description'], info['price'])
        self.db.query_db(query)

    def destroy_product(self, id):
        query = "DELETE FROM products WHERE id='{}'".format(id)
        self.db.query_db(query)

    def update_product(self, info, id):
        
        query = "UPDATE products SET name='{}', description='{}', price={}, updated_at=NOW() WHERE id={}".format(info['name'], info['description'], info['price'], id)
        
        self.db.query_db(query)

    """
    Below is an example of a model method that queries the database for all users in a fictitious application

    def get_all_users(self):
        print self.db.query_db("SELECT * FROM users")

    Every model has access to the "self.db.query_db" method which allows you to interact with the database
    """

    """
    If you have enabled the ORM you have access to typical ORM style methods.
    See the SQLAlchemy Documentation for more information on what types of commands you can run.
    """
