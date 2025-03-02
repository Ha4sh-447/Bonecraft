import numpy as np
import cv2

img = cv2.imread('img.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
thresh[thresh.shape[0]-3:thresh.shape[0], 0:thresh.shape[1]] = 0
white = np.where(thresh == 255)

xmin, ymin, xmax, ymax = np.min(white[1]), np.min(white[0]), np.max(white[1]), np.max(white[0])
print(xmin, xmax, ymin, ymax)
crop = img[ymin:ymax+3, xmin:xmax]
mask = thresh[ymin:ymax+3, xmin:xmax] > 0

result = cv2.cvtColor(crop, cv2.COLOR_BGR2BGRA)
result[:, :, 3] = (mask * 255).astype(np.uint8)

output_path = 'screw_bone.png'
cv2.imwrite(output_path, result)
cv2.imshow("crop with transparency", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Image saved as {output_path}")
