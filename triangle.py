
class Triangle(object):
    """ A Triangle is encoded as the triple of the indexes of its vertices in the Vertex array"""
    def __init__(self,v1,v2,v3):
        self.__v_ids = [v1,v2,v3] # _v_ids will store the indexes of three extreme vertices
        self.__adj = [-1,-1,-1] # _adj will store the adjacent triangles
        self.__visit = False


    def get_TV(self,pos):
        try:
            return self.__v_ids[pos]
        except IndexError as e:
            raise e

    def get_TT(self,pos):
        return self.__adj[pos]

    def set_TV(self,pos,new_id):
        try:
            self.__v_ids[pos] = new_id
        except IndexError as e:
            raise e

    def set_TT(self, pos, adjID):
        self.__adj[pos] = adjID

    def next_triangle(self, center, current, pred):
        pos = self.vertex_index(center)
        if self.get_TT((pos+1)%3) == pred:
            pred = current
            current = self.get_TT((pos+2)%3)
        else:  # self.get_TT((pos+2)%3) == pred
            pred = current 
            current = self.get_TT((pos+1)%3)

    def get_TE(self, pos): # obtain the edge opposite to the vertex at pos. eg. the edge opposite to vertex V0 is V1V2
        v1 = self.get_TV((pos+1)%3)
        v2 = self.get_TV((pos+2)%3)
        e = [v1,v2]
        e.sort() # The sort() method sorts the list ascending by default.
        return tuple(e)


    def get_vertices_num(self):
        return 3

    def vertex_index(self,vid): # For the vid, this function will obtain the index inside a triangle corresponding to this vid
        for i in range(3):
            if self.__v_ids[i] == vid:
                return i
        print("Error")

    def __str__(self):
        return "%s %s %s"%(self.__v_ids[0],self.__v_ids[1],self.__v_ids[2])
