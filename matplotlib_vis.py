import numpy as np
import matplotlib.pyplot as plt


print("lets run")

x = np.random.random(100)*2
y = np.random.random(100)*5

# plt.scatter(x,y)
# plt.show()


# line chart
# when we have a time series data

year = [ 2015 + x for x in range(20)]
# weight = [80,65,34,56,90,89,81,54,87,86,85,90,69,66,89,81,83,69,90,100]
# plt.plot(year,weight,"r--",lw=3)
# plt.scatter(year,weight)
# plt.show()

language = ["c", "solidity", "java", "c++", "Rust"]
attention = [69,70,15,100,90]
# plt.bar(language,attention)
# plt.show()

#normal distribution
# ages = np.random.normal(20,2,1000)
# plt.hist(ages,
#          bins=[ages.min(),18,21,ages.max()])
# plt.show()


# ax = plt.axes(projection="3d")
#
# x_axis = np.random.random(100)
# y_axis = np.random.random(100)
# z_axis = np.random.random(100)
#
# ax.set_title("learning 3d")
# ax.set_xlabel("label for x axis")
# ax.set_ylabel("label for y axis")
# ax.set_zlabel("label for z axis")
#
# plt.scatter(x_axis,y_axis,z_axis)
# plt.show()



ax = plt.axes(projection="3d")

x_axis = np.arange(1,11,0.1)
y_axis = np.sin(x)
z_axis = np.cos(x)

# ax.set_title("learning 3d")
# ax.set_xlabel("label for x axis")
# ax.set_ylabel("label for y axis")
# ax.set_zlabel("label for z axis")

plt.plot(x_axis,y_axis,z_axis)
plt.show()


