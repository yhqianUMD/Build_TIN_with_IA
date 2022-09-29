from operator import truediv
import sys  # sys.stdout.write

from vertex import Vertex
from triangle import Triangle

class TIN(object):
    '''Creates Class tree'''
    def __init__(self):
        self.__vertices=[]
        self.__triangles=[]


    def get_vertex(self,pos):
        try:
            return self.__vertices[pos]
        except IndexError as e:
            raise e

    def get_vertices_num(self):
        return len(self.__vertices)

    def get_triangle(self,pos):
        try:
            return self.__triangles[pos]
        except IndexError as e:
            raise e

    def get_triangles_num(self):
        return len(self.__triangles)

    def add_vertex(self,v):
        self.__vertices.append(v)

    def add_triangle(self,t):
        self.__triangles.append(t)

    def build(self): # this function will obtain partial VT relation and all TT relation
        ET = dict()
        for i in range(0,self.get_triangles_num()):
            tri = self.__triangles[i]
            for k in range(0,3):
                # tri.get_TV(k) is the k-th vertex ID; get_vertex(tri.get_TV(k)) is the corresponding vertex; get_vtstar() is one of the triangle ID incident in this vertex
                if self.get_vertex(tri.get_TV(k)).get_vtstar() == -1: 
                    self.get_vertex(tri.get_TV(k)).set_vtstar(i) # the if will guarantee that one of the incident triangle ID will be stored for each vertex; that's partial VT

                e = tri.get_TE(k) # e is the edge opposite to vertex k
                if e not in ET:
                    ET[e] = i # i is the triangle index incident in edge e
                else:
                    tri.set_TT(k,ET[e]) # set previous triangle as one adjacent triangle of current triangle
                    adj_tri = self.get_triangle(ET[e])
                    index = 3-(adj_tri.vertex_index(e[0])+adj_tri.vertex_index(e[1]))
                    self.get_triangle(ET[e]).set_TT(index,i) # set current triangle as one adjacent triangle of previous triangle
                    ET.pop(e) # remove edge e from ET{}

    def VT(self,center):
        # center is the vertex ID
        vt_list = []
        is_border = False
        pred = -1
        current = self.get_vertex(center).get_vtstar() # current is the triangle ID incident in the vertex center and stored in the vertex center; that's partial VT

        vt_list.append(current)
        # if we know that the position of center in a triangle is k
        k = self.get_triangle(current).vertex_index(center) #0,1,2
        pred = current
        # then the other two vertices are TV((k+1)%3) and TV((k+2)%3)
        current = self.get_triangle(current).get_TT((k+1)%3)
        while current != self.get_vertex(center).get_vtstar():
            if current == -1:
                if is_border==True:
                    break
                else:
                    is_border = True
                    pred = self.get_vertex(center).get_vtstar()
                    k = self.get_triangle(pred).vertex_index(center)
                    current = self.get_triangle(pred).get_TT((k+2)%3)
                    if current == -1:
                        break
            vt_list.append(current)
            # get next triangle
            cur_tri = self.get_triangle(current)
            pos = cur_tri.vertex_index(center)

            # cur_tri is the real triangle object
            # current is the triangle ID
            if cur_tri.get_TT((pos+1)%3) == pred:
                pred = current
                current = cur_tri.get_TT((pos+2)%3)
            else:#if cur_tri.get_TT((pos+2)%3) == pred:
                pred = current 
                current = cur_tri.get_TT((pos+1)%3)        
        
        return vt_list


    

    def VV(self,center):
        vv_list = []
        pred = -1
        current = self.get_vertex(center).get_vtstar()
        k = self.get_triangle(current).vertex_index(center)
        vv_list.append(self.get_triangle(current).get_TV((k+2)%3))
        pred = current
        current = self.get_triangle(current).get_TT((k+1)%3)
        is_border = False

        while current != self.get_vertex(center).get_vtstar():
            if current == -1:
                if is_border:
                    break
                else:
                    is_border = True
                    pred = self.get_vertex(center).get_vtstar()
                    tri = self.get_triangle(pred)
                    k = tri.vertex_index(center)
                    vv_list.append(tri.get_TV((k+1)%3))
                    current = self.get_triangle(pred).get_TT((k+2)%3)
                    if current == -1:
                        break
        
            cur_tri = self.get_triangle(current)

            pos = cur_tri.vertex_index(center)
            if cur_tri.get_TT((pos+1)%3) == pred:
                vv_list.append(cur_tri.get_TV((pos+1)%3))
                pred = current
                current = cur_tri.get_TT((pos+2)%3)
            else:  # self.get_TT((pos+2)%3) == pred
                vv_list.append(cur_tri.get_TV((pos+2)%3))
                pred = current 
                current = cur_tri.get_TT((pos+1)%3)          

        return vv_list  



