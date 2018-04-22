import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_product, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_product) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_product, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_product) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_product, **k):

    @staticmethod
    def POST_DELETE(id_product, **k):
    '''

    def GET(self, id_product, **k):
        message = None # Error message
        id_product = config.check_secure_val(str(id_product)) # HMAC id_product validate
        result = config.model.get_products(int(id_product)) # search  id_product
        result.id_product = config.make_secure_val(str(result.id_product)) # apply HMAC for id_product
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_product, **k):
        form = config.web.input() # get form data
        form['id_product'] = config.check_secure_val(str(form['id_product'])) # HMAC id_product validate
        result = config.model.delete_products(form['id_product']) # get products data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_product = config.check_secure_val(str(id_product))  # HMAC user validate
            id_product = config.check_secure_val(str(id_product))  # HMAC user validate
            result = config.model.get_products(int(id_product)) # get id_product data
            result.id_product = config.make_secure_val(str(result.id_product)) # apply HMAC to id_product
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/products') # render products delete.html 
