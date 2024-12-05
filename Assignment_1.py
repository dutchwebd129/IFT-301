#NAME: MOJIBAYO SINDARA DANIEL
#MATRIC NO: RUN/IFT/2/13191

import matplotlib.pyplot as pl

items = ['Spinach', 'Sausage', 'Prawns', 'Pineapple', 'Mushroom']
proportions = [0.27, 0.20, 0.12, 0.18, 0.15]
pl.barh(items, proportions, color='purple')
pl.xlabel('Proportion of Total')
pl.ylabel('Items')
pl.title('Proportions of Items')
pl.show()
