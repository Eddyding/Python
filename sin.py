import numpy as np
import matplotlib.pyplot as pt


x = np.arange(0,360)

y = np.sin(x * np.pi/180.0)


pt.plot(x,y,label="sin(x)")

#pt.plot(x,y)#label="sin(x)")


pt.xlim(0,360)
pt.ylim(-1.1,1.1)

pt.title("SIN function")
pt.legend()

pt.grid(True)


pt.savefig("figure/1.png",dpi=72)



pt.show()



