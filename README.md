# Bonecraft

## Problem statement
Traditional 2D X-rays limit diagnostic precision due to their lack of depth, slowing complex bone assessments, whereas our  3D reconstruction system transforms these images into interactive, high-resolution models using AI providing an alternative to costly CT scans and manual methods by offering a more affordable, and collaborative diagnostic tool.

## Approach

## 1. Frontend (User Interaction & Upload)  
The frontend serves as the user interface, enabling seamless interaction and data input for medical professionals.

- **User Authentication**  
  - Supports login for:  
    - **Individuals**: Verified specialists (e.g., radiologists, surgeons).  
    - **Organizations**: Medical centers or healthcare institutions.  
  - Ensures secure access with role-based permissions.

- **X-ray Image Upload**  
  - **Supported Formats**: `.png`, `.jpeg`, `.dicom`.  
  - **Features**: Real-time image preview before processing, allowing users to verify uploads.  
  - **Objective**: Provides an intuitive entry point for uploading patient X-rays.

## 2. Backend Processing (3D Reconstruction Pipeline)  
The backend powers the core 3D reconstruction process, leveraging advanced algorithms and computational techniques.

- **Image Processing**  
  - Enhances image quality (e.g., noise reduction, contrast adjustment).  
  - Extracts relevant bone structures for further analysis.  

- **Pose Estimation**  
  - Identifies bone orientation and joint positions using the YOLOv7pose model.  
  - Offers real-time accuracy without deep learning overhead, optimizing performance.  

- **Novel View Synthesis**  
  - Generates multiple computational perspectives (e.g., rotations, flips) from a single X-ray.  
  - Achieved without deep learning, ensuring efficiency and scalability.  

- **Depth Estimation**  
  - Computes depth maps and spatial relationships to construct realistic 3D structures.  
  - Utilizes point cloud generation as a foundational step.  

- **Mesh Reconstruction**  
  - Converts depth maps into low-poly 3D meshes for rendering.  
  - Balances detail and computational feasibility.  

- **Rendering and Exporting**  
  - Displays interactive 3D models with dynamic viewing options.  
  - Allows saving of models in compatible formats for further use.

## Results

#### Original Image
<img src="/result/original_image.jpeg" alt="Original image" width="50%">

#### Generated Views
![Alternate views](/result/novel_3d_views%20(1).png)


#### Depth Estimation
![Depth_analysis](/result/depth.png)

#### 3D Bone Structure
![3D bone view](/[result/point_cloud.gif](https://github.com/Ha4sh-447/Bonecraft/blob/main/result/point_cloud.gif))

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
