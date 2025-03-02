import cv2
import numpy as np

img = cv2.imread('screw_bone.png', cv2.IMREAD_UNCHANGED)
gray = cv2.cvtColor(img[:, :, :3], cv2.COLOR_BGR2GRAY)
alpha = img[:, :, 3]

h, w = gray.shape
x, y = np.meshgrid(np.arange(w), np.arange(h))
x = x.flatten()
y = y.flatten()

z = (gray.flatten() / 255.0) * 250.0

mask = alpha.flatten() > 0

x = x[mask]
y = y[mask]
z = z[mask]

points = np.column_stack((x, y, z))

np.savetxt('point_cloud.txt', points, fmt='%.6f', header='x y z', comments='# ')

print("Point cloud saved as point_cloud.txt")