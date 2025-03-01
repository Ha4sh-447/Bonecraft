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
<img src="https://ibb.co/HTKM3Jyw" alt="Fracture bone image" width="400"/>

#### Generated Views
<img src="https://ibb.co/r29c3bN0" alt="Alternate views" width="400"/>

#### Depth Estimation
<img src="https://ibb.co/4gFPdGZg" alt="Depth analysis" width="400"/>

#### 3D Bone Structure
![Working](https://gifyu.com/image/bbMdZ)
