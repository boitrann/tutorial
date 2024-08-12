import json
Movie = json.load(open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\movie\movies.json'))

def update_thongtin():
    with open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\movie\movies.json','w+',encoding='utf-8') as f:
        json.dump(Movie, f, indent= 3)
class Movies:
    def __init__(self,truyenvao) -> None:
        self.phim = truyenvao
    
    def get_info(self,phimnao):
        thong_tin = Movie[self.phim][phimnao]
        return thong_tin
    
    def get_id(self,phimnao):
        id = Movie[self.phim][phimnao]['id']
        return id
    
    def get_director(self,phimnao):
        director = Movie[self.phim][phimnao]['director']
        return director
    def edit_info(self,key_edit,value_edit,phimnao):
        if key_edit in Movie[self.phim][phimnao]:
            Movie[self.phim][phimnao][key_edit] = value_edit
            update_thongtin()
        else:
            print("Không có thông tin cần sửa")

    
    
if __name__ == "__main__":
    phim = Movies(truyenvao="movies")
    # thong_tin= phim.get_info(phimnao =0)
    # print(thong_tin)

    id = phim.get_id(phimnao=1)
    print(id)
    phim.edit_info(key_edit="id", value_edit= 2,phimnao=1)