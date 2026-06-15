========================================================================
             CS661 - ASSIGNMENT 1 EXECUTION INSTRUCTIONS
========================================================================

Group Number: 31
Members: Arnab Patra - 240186
         Akshita - 240090
         Nishant Singh - 230706

Requirements:
  - Python 3.x
  - VTK Library (Install via: pip install vtk)

Data Dependencies:
  - Task 1 requires "Isabel_2D.vti" to be present in the execution folder.
  - Task 2 requires "Isabel_3D.vti" to be present in the execution folder.

------------------------------------------------------------------------
TASK 1: 2D Isocontour Extraction
------------------------------------------------------------------------
File Name: part1_isocontour.py

Description:
This program extracts line-segment boundaries from a 2D uniform grid based 
on a user-provided isovalue threshold. The algorithm processes cells from 
scratch without utilizing built-in VTK extraction filters, traversing 
vertices in a strict counterclockwise (CCW) order starting from the 
bottom edge.

Command Format:
    python part1_isocontour.py <isovalue>

Parameters:
    <isovalue> : A floating-point number within the range [-1438, 630]

Example Execution:
    python part1_isocontour.py -500.0

Output:
Generates a file named 'extracted_contour.vtp' in the working directory.
To visualize the result:
  1. Open the file in ParaView and click 'Apply'.
  2. Change the solid color representation to Black, Red, or Blue 
     (especially if your ParaView canvas background is set to white) 
     to inspect the geometry clearly.

------------------------------------------------------------------------
TASK 2: VTK Volume Rendering
------------------------------------------------------------------------
File Name: part2_volume_render.py

Description:
This program uses a vtkSmartVolumeMapper to implement a 3D ray-casting 
volume visualization. It applies custom piecewise transfer functions for 
color mapping and opacity as dictated by the project parameters, adds a 
clean bounding box outline, and exposes a toggle switch for Phong Shading 
effects (Ambient/Diffuse/Specular parameters locked to 0.5).

Command Format:
    python part2_volume_render.py <yes/no>

Parameters:
    yes : Enables Phong Shading (realistic highlights/lighting calculations)
    no  : Disables shading effects (flat rendering profile)

Example (With Shading):
    python part2_volume_render.py yes

Example (Without Shading):
    python part2_volume_render.py no

Output:
Launches a dedicated 1000x1000 interactive rendering window on a clean 
white background. 
  - To change perspectives or rotate between the front and back views, 
    Left-Click and hold anywhere inside the window, then drag your cursor.
  - To exit the viewer, press 'q' or close the application window.
========================================================================
