class Item:
    
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        
        if self.price <= 0:
            raise ValueError("Invalid value for price, got {}".format(self.price))
            
    def __str__(self):
        return ("{}@{}-{}".format(self.name, self.price, self.category))
            
class Query:
    
    def __init__(self, field, operation, value):
        self.field = field
        self.operation = operation
        self.value = value
        operators = ["IN", "EQ", "GT", "GTE", "LT", "LTE", "STARTS_WITH", "ENDS_WITH", "CONTAINS"]
    
        if self.operation not in operators:
            raise ValueError("Invalid value for operation, got {}".format(self.operation))
        
    def __str__(self):
        return ("{} {} {}".format(self.field, self.operation, self.value))
        
class Store:
    
    def __init__(self):
        self.list_items = []
    
    def add_item(self, item):
        self.list_items.append(item)
        
    def __str__(self):
        if len(self.list_items)!= 0:
            return "\n".join(map(str, self.list_items))
        else:
            return "No items"
            
    def filter(self, query):
        new_list = Store()
        
        for item in self.list_items:
            a = getattr(item, query.field)
            
            if query.operation == "IN" and a in query.value:
                new_list.add_item(item)
                
            elif query.operation == "EQ" and a == query.value:
                new_list.add_item(item)
                
            elif query.operation == "GT" and a > query.value:
                new_list.add_item(item)
                
            elif query.operation == "GTE" and a >= query.value:
                new_list.add_item(item)
                
            elif query.operation == "LT" and a < query.value:
                new_list.add_item(item)
                
            elif query.operation == "LTE" and a <= query.value:
                new_list.add_item(item)
                
            elif query.operation == "STARTS_WITH" and a.startswith(query.value):
                new_list.add_item(item)
            
            elif query.operation == "ENDS_WITH" and a.endswith(query.value):
                new_list.add_item(item)
                
            elif query.operation == "CONTAINS" and query.value in a:
                new_list.add_item(item)
        return new_list
        
    def count(self):
        return len(self.list_items)
        
    def exclude(self, query):
        exclude_list = Store()
        filter_query = self.filter(query)
        for item in self.list_items:
            if item not in filter_query.list_items:
                exclude_list.add_item(item)
        return exclude_list