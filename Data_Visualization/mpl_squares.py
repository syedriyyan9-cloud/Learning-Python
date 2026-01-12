import matplotlib.pyplot as plt

# squares = [number*number for number in range(6)]
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
# print(plt.style.available)
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(input_values,squares,linewidth = 3)
ax.set_title('Square Numbers',fontsize=24)
ax.set_xlabel('Value',fontsize=14)
ax.set_ylabel('Square of Values',fontsize=14)
ax.tick_params('both',labelsize=14)
plt.show()