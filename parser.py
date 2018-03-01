from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    open_file = open(fname, 'r')
    file_lines = open_file.readlines()
    for i in range(0,len(file_lines)):
        if(file_lines[i] == "line\n"):
            coords = file_lines[i+1].split()
            add_edge(points, int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]), int(coords[4]), int(coords[5]))
        if(file_lines[i] == "display\n"):
            draw_lines(points, screen, color)
            display(screen)
        if(file_lines[i] == "ident\n"):
            transform = ident(transform)
        if(file_lines[i] == "scale\n"):
            scales = file_lines[i+1].split()
            scale_matrix = [[int(scales[0]), int(scales[1]), int(scales[2])]]
            matrix_mult(transform, scale_matrix)
            
        else:
            print file_lines[i]
    pass
