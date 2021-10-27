import sympy as sp
from sympy.interactive.printing import init_printing
from progress.bar import Bar

def calcular(n):
    x, t, a, b = sp.symbols('x t a b')
    v_0 = sp.E**x
    f_0 = v_0*(v_0-a)*(1-v_0)
    w_0 = sp.diff(sp.diff(v_0,x),x)-f_0
    bar = Bar('Processing', max=n)
    try:
        for i in range(n):
            v = v_0-sp.integrate(sp.diff(v_0,t)-sp.diff(sp.diff(v_0,x),x)+f_0+w_0,(t,0,t))
            w = w_0-sp.integrate(sp.diff(sp.diff(w_0,t),t)-b*v_0,t)

            v_0 = v
            w_0 = w
            bar.next()
        bar.finish()
    except KeyboardInterrupt:
        pass
    return v, w

if __name__=='__main__':
    init_printing(use_unicod=True)
    v, w = calcular(20)
    f = open('i_20_v','a')
    f.write(str(v))
    f.close()
    f = open('i_20_w','a')
    f.write(str(w))
    f.close()