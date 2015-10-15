from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn2, venn2_circles
plt.figure(figsize=(12,12), facecolor="white")
#syntax: set1, set2, set1x2...
subset_tuple=(9,4,2)
v = venn2(subsets=subset_tuple, set_labels = ('A', 'B', 'C'))

v.get_patch_by_id('100').set_alpha(0.1)
v.get_patch_by_id('100').set_color('gray')
v.get_patch_by_id('110').set_color('green')
v.get_patch_by_id('110').set_alpha(0.7)
v.get_patch_by_id('010').set_alpha(0.4)
v.get_label_by_id('100').set_text('Set of all qualia')
v.get_label_by_id('010').set_text('Set of all concurrent\n mental processes')
v.get_label_by_id('110').set_text('Consciousnes')
v.get_label_by_id('A').set_text('')

c = venn2_circles(subsets=subset_tuple)
c[0].set_ls('dotted')
c[1].set_ls('dashed')
plt.title("Venn Diagram of Consciousnes")

from matplotlib.transforms import Affine2D
ax = plt.gca()
center = [np.mean(ax.get_xlim()), np.mean(ax.get_ylim())]
t = Affine2D().rotate_deg_around(center[0], center[1], 90) + ax.transData
for v in ax.patches + ax.texts:
	v.set_transform(t)
yl = ax.get_ylim()
plt.ylim(yl[0]-0.2, yl[1]+0.2)

plt.show()
