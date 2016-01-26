"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        products = self.models['Product'].get_all_products()
        return self.load_view('index.html', products=products)

    def new(self):
        return self.load_view('newproduct.html')

    def edit(self, id):
        product_info = self.models['Product'].get_product_info(id)
        return self.load_view('editproducts.html', product_info=product_info[0])


    def show(self, id):
        print '*' * 50

        product_info = self.models['Product'].get_product_info(id)
        
        return self.load_view('productinfo.html', product_info=product_info[0])

    def create(self):
        ismoney = self.models['Product'].check_price(request.form['price'])
        
        if not ismoney:
            flash('Your price must be formatted properly. Ex: 19.99')
        else:
            product_info = {
            'name' : request.form['name'],
            'description' : request.form['description'],
            'price' : request.form['price']
            }

            self.models['Product'].create_product(product_info)
        return redirect('/')

    def destroy(self):
        self.models['Product'].destroy_product(request.form['id'])
        return redirect('/')

    def update(self, id):
        product_info = {
        'id' : id,
        'name' : request.form['name'], 
        'description' : request.form['description'], 
        'price' : request.form['price']
        }

        self.models['Product'].update_product(product_info, id)
        
        return redirect('/products/show/'+str(id))
