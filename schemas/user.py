def serializDict(item)-> dict:
    return{
        'id':str(item['_id']),
        'name':(item['name']),
        'email':(item['email']),
        'password':(item['password']),
    }
    
    
def serializList(entity)->list:
    return [serializDict(item) for item in entity]


def serializDict(a)-> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}



def serializList(entity)-> list:
    return [serializDict(a) for a in entity]