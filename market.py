import pylab as pl

def profit(x, y, z):
    return (60 - x**(2/3)/100 - y**(2/3)/100 - z**(2/3)/100) * x**(2/3) - 2*x

def profit_collusion(x):
    return (60 - 3*x**(2/3)/100) * x**(2/3) - 2*x
    
def plot_profit():
    minx = 0
    maxx = 10000
    miny = 0
    maxy = maxx/2
    resolution=201
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    X = np.linspace(minx, maxx, resolution)
    Y = np.linspace(miny, maxy, resolution)
    Z = np.array([profit(x,y,y) for j, y  in enumerate(Y) for i, x in enumerate(X)])
    
    X, Y = np.meshgrid(X, Y)
    Z = Z.reshape(resolution, resolution)
    
    plt.pcolor(X, Y, Z)
    plt.show()
    
def equilibrium():
    x = 400
    y = 2000
    z = 3000
    increment = 0.1
    iterations = 50000
    X = [0 for _ in range(iterations)]
    Y = [0 for _ in range(iterations)]
    Z = [0 for _ in range(iterations)]
    PX = [0 for _ in range(iterations)]
    PY = [0 for _ in range(iterations)]
    PZ = [0 for _ in range(iterations)]
    I = [i for i in range(iterations)]
    for i in range(iterations):
        if profit(x+increment, y, z) > profit(x,y,z):
            x+=increment
        elif x>0 and profit(x-increment, y, z) > profit(x,y,z):
            x-=increment
        X[i] = x
        PX[i] = profit(x,y,z)
    
        if profit(y+increment, x, z) > profit(y,x,z):
            y+=increment
        elif y>0 and profit(y-increment, x, z) > profit(y,x,z):
            y-=increment
        Y[i] = y
        PY[i] = profit(y,x,z)

        if profit(z+increment, x, y) > profit(z,x,y):
            z+=1
        elif z>0 and profit(z-increment, x, y) > profit(z,x,y):
            z-=increment
        Z[i] = z
        PZ[i]=profit(z,x,y)
       
    pl.figure(figsize=(14,6))
    pl.plot(I, X, "b")
    pl.plot(I, Y, "g")
    pl.plot(I, Z, "r")
    
    print(x,y,z)
    print(profit(x,y,z), profit(y,x,z), profit(z,x,y))
    pl.show()            
               

def collusion():
    max_quantity = 6000
    I = [i for i in range(max_quantity)]
    X=[profit_collusion(i) for i in range(max_quantity)]
    pl.figure(figsize=(14,6))
    pl.plot(I, X, "b")
    
    pmax = max(X)
    qmax = X.index(pmax)
    print(qmax, pmax)
    pl.show()
        
if __name__ == "__main__":
    equilibrium()
    collusion()
    
