import numpy as np
import matplotlib.pyplot as pt



x = np.arange(0,360)

y = np.sin(2*x * np.pi / 180.0)

z = np.cos(x * np.pi / 180.0)



pt.plot(x,y,color="blue",label="SIN(2X)")
pt.plot(x,z,color="red",label = "COS(X)")

pt.xlim(0,360)
pt.ylim(-1.2,1.2)
pt.xlabel("Degree")
pt.ylabel("Value")

pt.title("SIN & COS function")
pt.legend()

pt.show()

pt.savefig("figure/2.png",dpi=80)


