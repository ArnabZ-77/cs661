CS661 - Assignment 1 Execution Instructions

Group Number: [Insert Group Number]
Members: [Insert Member Names]

Requirements:
- Python 3.x
- VTK Library (pip install vtk)

--------------------------------------------------
TASK 1: 2D Isocontour Extraction
--------------------------------------------------
To run the 2D Isocontour extraction script, provide an isovalue (range -1438 to 630) as a command line argument.

Command Format:
python part1_isocontour.py <isovalue>

Example:
python part1_isocontour.py -500

Output:
Generates an 'extracted_contour.vtp' file in the directory, which can be visualized in ParaView.

--------------------------------------------------
TASK 2: VTK Volume Rendering
--------------------------------------------------
To run the 3D volume rendering script, specify whether you want Phong Shading enabled by providing 'yes' or 'no' as an argument.

Command Format:
python part2_volume_render.py <yes/no>

Example with Shading:
python part2_volume_render.py yes

Example without Shading:
python part2_volume_render.py no

Output:
Launches a 1000x1000 interactive window rendering the volumetric data with an outline.