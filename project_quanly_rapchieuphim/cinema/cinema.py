import json
Cinema = json.load(open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\cinema\cinemas.json',encoding='utf-8'))

def update_cinema():
    with open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\cinema\cinemas.json','w+',encoding='utf-8') as f:
        json.dump(Cinema,f,indent=2)
class Cinemas:
    def __init__(self,truyenvao) -> None:
        self.cine= truyenvao
    
    def get_info(self,rapnao,rap_may,ghenao):
        tinh_trang_ghe = Cinema[self.cine][rapnao]["cinemaRooms"][rap_may]["seats"][ghenao]["status"]
        return tinh_trang_ghe
    
if __name__=="__main__":
    rap = Cinemas(truyenvao="cinemas")
    tinh_trang_ghe = rap.get_info(rapnao=0,rap_may=0,ghenao=0)
    print(tinh_trang_ghe)