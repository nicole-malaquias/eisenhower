class ImportanceErrors(Exception):
    
    def __init__(self, data):
                
            self.message = {
            "error":{"valid_options":{
                        "importance":[1,2],
                        "urgency":[1,2]},
                    
                },
            "recieved_options":{
                "importance":data['importance'],
                "urgency": data['urgency']
            } 
        }
            super().__init__(self.message)
