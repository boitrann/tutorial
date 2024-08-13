import json
movie = json.load(open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\movie\movies.json'))

def update_thongtin():
    with open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\movie\movies.json','w+',encoding='utf-8') as f:
        json.dump(movie, f, indent= 3)

class movies:
    def __init__ (self,movie_catgory) -> None:
       self.movie_ =movie_catgory
    
    def get_info(self,movie_no):
        movie_info = movie[self.movie_][movie_no]
        return movie_info
    
    def get_id(self,movie_no):
        id = movie[self.movie_][movie_no]['id']
        return id
    
    def get_director(self,movie_no):
        director = movie[self.movie_][movie_no]['director']
        return director
    
    def edit_info(self,key_edit,value_edit,movie_no):
        if key_edit in movie[self.movie_][movie_no]:
            movie[self.movie_][movie_no][key_edit] = value_edit
            update_thongtin()
        else:
            print("Không có thông tin cần sửa")

    
    
if __name__ == "__main__":
    phim = movies(movie_catgory="movies")
    movie_info= phim.get_info(movie_no =2)
    print(movie_info)

    id = phim.get_id(movie_no=0)
    # print(id)
    phim.edit_info(key_edit="id", value_edit= 2,movie_no=1)
    