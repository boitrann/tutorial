import json
Cinema = json.load(open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\cinema\cinemas.json',encoding='utf-8'))

def update_cinema():
    with open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\cinema\cinemas.json','w+',encoding='utf-8') as f:
        json.dump(Cinema,f,indent=2)
class Cinemas:
    def __init__(self,truyenvao) -> None:
        self.cine= truyenvao
    
print(Cinema[cinemas])