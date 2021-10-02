class FieldError(Exception):

    
    def __init__(self, data):
        
        data = list(data)
        problem = [ i for i in data if i not in ['categories','name','description','duration','importance','urgency'] ]
        
        self.message = {
            "available_keys": [
               'categories','name','description','duration','importance','urgency',
                ],
            "Wrong_keys_sended": [*problem]          
        }
        super().__init__(self.message)