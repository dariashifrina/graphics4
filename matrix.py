import math

def make_translate( x, y, z ):
    translate_matrix = [[1, 0, 0, x], [0,1,0,y], [0,0,1,z], [0, 0, 0, 1]] 
    return translate_matrix

def make_scale( x, y, z ):
    scale_matrix = [[x, 0, 0, 0], [0,y,0,0], [0,0,z,0], [0,0,0,1]]
    return scale_matrix

def make_rotX( theta ):
    angle = math.radians(theta)
    anglesin = math.sin(angle)
    anglecos = math.cos(angle)
    rotX_matrix = [[1, 0, 0, 0],[0, anglecos, -1 * anglesin, 0], [0, anglesin, anglecos, 0], [0,0,0,0]]
    pass

def make_rotY( theta ):
    angle = math.radians(theta)
    anglesin = math.sin(angle)
    anglecos = math.cos(angle)
    rotY_matrix = [[anglecos, 0, anglesin, 0],[0,1,0,0],[-1 * anglesin, 0, anglecos, 0], [0,0,0,0]]
    pass

def make_rotZ( theta ):
    angle = math.radians(theta)
    anglesin = math.sin(angle)
    anglecos = math.cos(angle)
    rotZ_matrix = [[angelcos, -1 * anglesin, 0, 0],[anglesin, anglecos, 0, 0],[0,0,1,0], [0,0,0,1]]
    return rotZ_matrix

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
