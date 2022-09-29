import sys  # sys.stdout.write
import os
from tin import TIN
from vertex import Vertex
from triangle import Triangle
import csv
import time

def read_tin_file(url_in):
    with open(url_in) as infile:
        tin = TIN()

        trash = infile.readline()
        line = (infile.readline()).split()
        vertices_num = int(line[0])
        triangles_num = int(line[1])
        print("vnum: {}, tnum:{}".format(vertices_num, triangles_num))

        for l in range(vertices_num):
            line = (infile.readline()).split()
            v=Vertex(float(line[0]),float(line[1]),float(line[2]))
            tin.add_vertex(v)

        for l in range(triangles_num):
            line = (infile.readline()).split()
            t=Triangle(int(line[1]),int(line[2]),int(line[3]))
            tin.add_triangle(t)
        infile.close()
        return tin


if __name__ == '__main__':
    # read vertices and triangles from off file
    tin_file = sys.argv[1]
    tin = read_tin_file(tin_file)
    # build IA data structure
    tin.build()

    t0 = time.time()
    # obtain IA based data -- vertex
    out_file_vertex = sys.argv[2]    
    with open(out_file_vertex, 'w', newline='') as ofs:
        writer = csv.writer(ofs)
        for vid in range(tin.get_vertices_num()):
            test_ver = tin.get_vertex(vid)
            # output each vertex as x,y,ele,VID,tID
            # writer.writerow("{} {} {} {} {}\n".format(
            #    test_ver.get_c(0), test_ver.get_c(1), test_ver.get_c(2), vid, test_ver.get_vtstar()))
            writer.writerow(
                [test_ver.get_c(0), test_ver.get_c(1), test_ver.get_c(2), vid, test_ver.get_vtstar()])

    t1 = time.time()
    print("time cost to output vertices:", t1-t0)

    t2 = time.time()
    # obtain IA based data -- triangle
    out_file_tri = sys.argv[3]
    with open(out_file_tri, 'w', newline='') as ofs:
        writer = csv.writer(ofs)
        for tid in range(tin.get_triangles_num()):
            test_tri = tin.get_triangle(tid)
            # output each triangle as x1,y1,x2,y2,x3,y3,x1,y1,v1,v2,v3,t_self,t1,t2,t3
            writer.writerow(
                [tin.get_vertex(test_tri.get_TV(0)).get_c(0), tin.get_vertex(test_tri.get_TV(0)).get_c(1), tin.get_vertex(test_tri.get_TV(1)).get_c(0), tin.get_vertex(test_tri.get_TV(1)).get_c(1), 
                tin.get_vertex(test_tri.get_TV(2)).get_c(0), tin.get_vertex(test_tri.get_TV(2)).get_c(1), tin.get_vertex(test_tri.get_TV(0)).get_c(0), tin.get_vertex(test_tri.get_TV(0)).get_c(1), 
                test_tri.get_TV(0), test_tri.get_TV(1), test_tri.get_TV(2), tid, 
                test_tri.get_TT(0), test_tri.get_TT(1), test_tri.get_TT(2)])

    t3 = time.time()
    print("time cost to output triangles:", t3-t2)
    '''
    for vid in range(tin.get_vertices_num()):
        test_ver = tin.get_vertex(vid)
        print("Vertex "+str(vid)+"'s VTstar:")
        print(test_ver.get_vtstar())
        print("Vertex "+str(vid)+"'s VT:")
        print(tin.VT(vid))
        print("Vertex "+str(vid)+"'s VV:")
        print(tin.VV(vid))
    for tid in range(tin.get_triangles_num()):
        test_tri = tin.get_triangle(tid)
        print("triangle "+str(tid)+"'s TT")
        for i in range(0,3):
            print(str(test_tri.get_TV(i))+"'s TT:  "+str(test_tri.get_TT(i)))
    '''
