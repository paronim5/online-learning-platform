class DaoInterface:
    def get_all(self):
        raise NotImplementedError
    
    def get_by_id(self, id):
        raise NotImplementedError
    
    def save(self, object):
        raise NotImplementedError
    
    def update(self, id):
        raise NotImplementedError
    
    def delete(self, id):
        raise NotImplementedError