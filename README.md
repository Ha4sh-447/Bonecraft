# Bonecraft

## Problem statement
Develop a Generative AI-powered robotic system for various minimally invasive surgeries that provides enhanced dexterity, haptic feedback, and 3D visualization to improve surgical precision.

## Approach

### 1. **Frontend (User Interaction & Upload)**
   - **User Authentication**
     - Users can log in as individuals (verified specialists) or organizations (medical centers).
   - **X-ray Image Upload**
     - Supports file formats: `.png`, `.jpeg`, `.dicom`
     - Provides an image preview before processing.

### 2. **Backend Processing (3D Reconstruction Pipeline)**  
   - **Image Processing**
     - Enhances image quality and extracts relevant bone structures.
   - **Pose Estimation**
     - Identifies bone orientation and joint positions.
   - **Novel View Synthesis**
     - Generates multiple perspectives computationally (without deep learning).
   - **Depth Estimation**
     - Computes depth and spatial relationships to create a realistic 3D structure.
   - **Mesh Reconstruction**
     - Converts the depth map into a low-poly 3D mesh.
   - **Rendering and Exporting**
     - Displays and saves the 3D model.

### 3. **Generative AI Enhancement**
   - **Gen AI Upscaling**
     - Enhances the 3D model resolution.
   - **Existing 3D Renders**
     - Uses existing datasets to fine-tune AI models for better accuracy.

### 4. **Final Output**
   - Interactive 3D Model with:
     - Zooming and rotation
     - Annotation and collaboration features
     - Reporting tools for medical professionals.

## Results

#### Original Image
<img src="/result/original_image.jpeg" alt="Original image" width="50%">

#### Generated Views
![Alternate views](/result/novel_3d_views%20(1).png)


#### Depth Estimation
![Depth_analysis](/result/depth.png)

#### 3D Bone Structure
[3D bone view](/result/video.mp4)

## **Tech Stack**
### **Frontend**
- **Visualization & UI/UX:** Next.js (React), Three.js, Tailwind CSS  

### **Backend**
- **Libraries & Frameworks:** NumPy, TensorFlow, U-Net, OpenCV, Scipy, MiDaS v2.1 Small, ONNX Runtime, Open3D, MeshLab, OpenPose, Three.js  

### **Database**
- PostgreSQL / MongoDB  

### **Deployment**
- Docker & Kubernetes  

---

This project focuses on AI-powered **3D Reconstruction** from X-ray images, improving medical imaging and diagnosis with deep learning, computational vision, and interactive 3D visualization.
