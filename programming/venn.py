import matplotlib.pyplot as plt
from matplotlib_venn import venn2

venn2(subsets = (8, 10, 5), set_labels = ('AckerCode', 'Python'))
plt.show()
