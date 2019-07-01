import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib
matplotlib.style.use('ggplot')

x = [#2764, 
	88, 127, 112, 45, 31, 33, 100, 470, 31, 355, 91, 415, 384, 408]
y = [#3372405, 
	269673, 278926, 273979, 262036, 260829, 261341, 271844, 516986, 261406, 380109, 269025, 421835, 379965, 416373]

fig, ax = plt.subplots(1,1)
plt.scatter(x, y)
plt.xlabel('two strings input (bytes)')
plt.ylabel('memory usage (bytes)')
plt.tight_layout()
plt.show()