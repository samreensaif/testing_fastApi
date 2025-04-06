from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
names = {"Samreen":22, "Muhammad":87, "Rahul":19, "Naveed":23}

# get request

@app.get("/")

def get_request():
    
    new_names = [i.capitalize()+" having age " + str(j) for i,j in names.items()]
    return new_names


# post request


class Item(BaseModel):
    name: str
    age: int
    
@app.post("/")

def post_request(data:Item):

    names.update({data.name:data.age})
    # names[data.name]=data.age
    
    return names #names

# delete request

@app.delete("/{name}")


def delete_request(name: str):
    if name in names:
        age = names.pop(name)
        return {
            "message": f"{name} having age {age} is deleted successfully!!! 👌"
        }
    else:
        return {
            "error": f"{name} not found in records!"
        }


# put request

@app.put("/{name}")
def put_request(name: str, data: Item):
    
    for i in names:
        if i == name:
            names.pop(i)
            
            names[data.name]=data.age
            return {
                "message": f"{name} updated to name {data.name} and age {data.age} successfully! ✅",
                
            }

        
    
