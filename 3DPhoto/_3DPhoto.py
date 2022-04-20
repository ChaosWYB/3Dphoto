from mayavi import mlab
import numpy as np

def cube(x,y,z,a = 1):
    #用于生成一顶点在（x,y,z),边长为a的立方体
    #输入：
    #x,y,z  顶点坐标
    #a      立方体边长，默认值为1
    #return 立方体各定点坐标
    x_s = np.array([x,x,x,x,x+a,x+a,x+a,x+a])
    y_s = np.array([y,y,y+a,y+a,y,y,y+a,y+a])
    z_s = np.array([z,z+a,z,z+a,z,z+a,z,z+a])
    return x_s, y_s, z_s

def ball(x,y,z,r):
    #用于生成球心在（x,y,z），半径为r的球体
    #输入：
    #x,y,z  球心坐标
    #r      球体半径
    #return 球面各点坐标（选取角间隔为 pi / 50）

    x = np.array([])
    y = np.array([])
    z = np.array([])
    dtheta = np.pi / 25
    dphi = np.pi / 50
    dr = 0.1
    dz = 0.1
    r = 1
    phi = 0
    for i in range(50):
        theta = 0
        for j in range(50):
            p_x = r * np.sin(phi) * np.cos(theta)
            p_y = r * np.sin(phi) * np.sin(theta)
            p_z = r * np.cos(phi)
            x, y, z = append_points(x,y,z,p_x,p_y,p_z)
            theta += dtheta
        phi += dphi
    return x, y, z

def create_labels(s):
    #建立xyz坐标
    #s代表是否建立坐标
    if s:
        mlab.xlabel('x')    #x轴名称为x
        mlab.ylabel('y')    #y轴名称为y
        mlab.zlabel('z')    #z轴名称为z

def append_points(x,y,z,a,b,c):
    #分别将a,b,c添加到x,y,z数组中，返回新数组
    #输入：
    #x,y,z  选择要延伸的数组
    #a,b,c  选择要添加的数据
    #return 修改后的新x,y,z
    x = np.append(x,[a])
    y = np.append(y,[b])
    z = np.append(z,[c])
    return x, y, z

def init():
    #表格初始化
    mlab.figure(1, fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))

def create_cubes(points):
    #用于创建由多个立方体堆砌的复杂结构，并实现绘制图像
    #输入
    #points 复杂堆砌体中各个立方体点的信息
    #points为二维数组，其中
    #point[0],point[1],point[2],point[3]分别代表了立方体一顶点的x,y,z，和其边长a
    for point in points:
        x, y, z = cube(point[0],point[1],point[2],point[3])

        # 在空间中建立几何体各点坐标
        pts = mlab.points3d(x, y, z, z, scale_mode='none', scale_factor=0.01)
    
        # 相邻点进行连线，
        mesh = mlab.pipeline.delaunay3d(pts)

        #相邻连线建立平面
        surf = mlab.pipeline.surface(mesh)

def visualization(x,y,z):
    #实现空间中的建模
    #输入：
    #x,y,z      分别记录各个点的坐标，相同下标的x[i],y[i],z[i]确定一个点

    # 在空间中标记所有点
    pts = mlab.points3d(x, y, z, z, scale_mode='none', scale_factor=0.01)

    # 对三维空间中的点进行连线
    mesh = mlab.pipeline.delaunay3d(pts)

    # 将连线确定的面上色
    surf = mlab.pipeline.surface(mesh)

#主函数
if __name__ == "__main__":

    #绘制窗口初始化
    init()

    #导入模型定点的数据
    p = [[0,0,0,1],[0,1,0,1],[0,2,0,1],\
        [-1,2,0,1],[0,1,1,1]]
    
    #建模
    create_cubes(p)

    #p = [[0,0],[1,0],[2,0],[3,0],[5,0],[0.5,1],[1.5,1.1],[2.5,2]]
    #girder_2d(p)

    #p = [[0,0,0],[0,1,0],[1,0,0],[1,1,0],[2,0,0],[2,1,0],[0.5,0.5,1],[1.5,0.5,1]]
    #girder_3d(p)

    #x,y,z = cube(0,0,0,1)
    #visualization(x,y,z)

    #artwork2()

    #建立模型范围边框
    #mlab.outline()

    #创建坐标轴
    create_labels(False)

    #模型数据更新到窗口中
    mlab.show();
