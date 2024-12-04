#NAME: MOJIBAYO SINDARA DANIEL
#MATRIC NO: RUN/IFT/2/13191

import matplotlib.pyplot as plt

items = ['Spinach', 'Sausage', 'Prawns', 'Pineapple', 'Mushroom']
proportions = [0.27, 0.20, 0.12, 0.18, 0.15]
plt.barh(items, proportions, color='purple')
plt.xlabel('Proportion of Total')
plt.ylabel('Items')
plt.title('Proportions of Items')
plt.show()
