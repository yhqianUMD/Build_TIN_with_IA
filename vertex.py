from point import Point

class Vertex(Point):
    """ A Vertex is an extention of Class Point and takes (x,y) attributes plus an elevation."""
    def __init__(self,x,y,z):
        Point.__init__(self,x,y)
        self.__field_values = [z] 
        self.__vtstar = -1

    def get_z(self):
        return self.__field_values[0]

    def set_z(self,z):
        self.__field_values[0] = z

    def get_vtstar(self):
        return self.__vtstar
    
    def set_vtstar(self,tid):
        self.__vtstar = tid

    def get_c(self,pos):
        if pos in (0,1):
            return super().get_c(pos)
        else:
            try:
                return self.__field_values[pos-2]
            except IndexError as e:
                raise e

    def set_c(self,pos,c):
        if pos in (0,1):
            super().set_c(pos,c)
        else:
            try:
                self.__field_values[pos-2] = c
            except IndexError as e:
                # raise e
                # instead of raising an exception we append the field value to the end of the array
                self.__field_values.append(c)
    def get_last_field_item(self):
        return self.__field_values[-1]
    
    def get_fields_num(self):
        return len(self.__field_values)
    
    def add_field(self, f):
        self.__field_values.append(f)
    def get_field(self, pos):
        return self.__field_values[pos]
    def print_fields(self):
        for f in self.__field_values:
            print(f)

    def __str__(self):
        return "Vertex(%s,%s,%s)"%(self.get_x(),self.get_y(),self.get_z())
