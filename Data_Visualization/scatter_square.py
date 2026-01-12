import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [number**2 for number in x_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values,s=10,c=y_values,cmap=plt.cm.Reds)
ax.axis([0,1100,0,1100000])
ax.set_title('Square Numbers',fontsize=24)
ax.set_xlabel('Value',fontsize=14)
ax.set_ylabel('Square of Values',fontsize=14)
ax.tick_params('both',which = 'major', labelsize=14)
plt.show()