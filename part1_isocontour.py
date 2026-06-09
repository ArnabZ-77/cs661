import sys
import vtk

def main():
    # 1. Read the command-line argument for the isovalue
    if len(sys.argv) < 2:
        print("Usage: python part1_isocontour.py <isovalue>")
        return
    
    isovalue = float(sys.argv[1])
    print(f"Extracting isocontour for value: {isovalue}") # [cite: 70]

    # 2. Load the 2D data file using VTK [cite: 6, 16]
    reader = vtk.vtkXMLImageDataReader() # or vtkStructuredPointsReader depending on your file
    reader.SetFileName("Isabel_2D.vti") # Update with actual file path [cite: 6]
    reader.Update()
    
    data = reader.GetOutput()
    dims = data.GetDimensions() # Get X, Y, Z grid sizes [cite: 5]
    scalars = data.GetPointData().GetScalars() # Fetch the Pressure values [cite: 30]

    # 3. Create VTK elements to store the final output [cite: 7, 20]
    points = vtk.vtkPoints()
    cell_array = vtk.vtkCellArray() # [cite: 20]

    # Helper function to get point index in a uniform grid
    def get_point_index(i, j):
        return j * dims[0] + i

    # 4. Traverse the 2D grid cells [cite: 5]
    # For a 2D grid slice, dims[2] is typically 1 (Z-axis loop is not needed)
    for j in range(dims[1] - 1):
        for i in range(dims[0] - 1):
            
            # 5. Get the 4 corner indices in Counterclockwise Order [cite: 19]
            # Starting from the bottom-left vertex [cite: 19]
            idx0 = get_point_index(i, j)       # Bottom-Left
            idx1 = get_point_index(i + 1, j)   # Bottom-Right
            idx2 = get_point_index(i + 1, j + 1) # Top-Right
            idx3 = get_point_index(i, j + 1)   # Top-Left

            # Get structural spatial coordinates
            p0 = data.GetPoint(idx0)
            p1 = data.GetPoint(idx1)
            p2 = data.GetPoint(idx2)
            p3 = data.GetPoint(idx3)

            # Get scalar values (Pressure) [cite: 30]
            v0 = scalars.GetTuple1(idx0)
            v1 = scalars.GetTuple1(idx1)
            v2 = scalars.GetTuple1(idx2)
            v3 = scalars.GetTuple1(idx3)

            # Define the 4 edges in counterclockwise order [cite: 19]
            # (Vertex A, Vertex B, Coord A, Coord B, Value A, Value B)
            edges = [
                (idx0, idx1, p0, p1, v0, v1), # Bottom edge [cite: 19]
                (idx1, idx2, p1, p2, v1, v2), # Right edge
                (idx2, idx3, p2, p3, v2, v3), # Top edge
                (idx3, idx0, p3, p0, v3, v0)  # Left edge
            ]

            cell_intersections = []

            # 6. Linear Interpolation to find edge intersections [cite: 19]
            for edge in edges:
                va, vb = edge[4], edge[5]
                # Check if the isovalue cuts through this edge
                if (va <= isovalue <= vb) or (vb <= isovalue <= va):
                    if va != vb: # Avoid division by zero
                        # Linear interpolation ratio t
                        t = (isovalue - va) / (vb - va)
                        # Compute exact intersection coordinate (x, y, z)
                        pa, pb = edge[2], edge[3]
                        x = pa[0] + t * (pb[0] - pa[0])
                        y = pa[1] + t * (pb[1] - pa[1])
                        z = pa[2] + t * (pb[2] - pa[2])
                        cell_intersections.append((x, y, z))

            # 7. Connect intersection points with lines [cite: 20]
            # If two intersections are found in this cell, build a segment line [cite: 20]
            if len(cell_intersections) == 2:
                pt_id1 = points.InsertNextPoint(cell_intersections[0])
                pt_id2 = points.InsertNextPoint(cell_intersections[1])
                
                line = vtk.vtkLine()
                line.GetPointIds().SetId(0, pt_id1)
                line.GetPointIds().SetId(1, pt_id2)
                cell_array.InsertNextCell(line) # [cite: 20]

    # 8. Save the extracted boundaries to a VTK PolyData file (*.vtp) [cite: 7, 22]
    polydata = vtk.vtkPolyData() # [cite: 7, 20]
    polydata.SetPoints(points)
    polydata.SetLines(cell_array) # [cite: 20]

    writer = vtk.vtkXMLPolyDataWriter() # [cite: 16, 22]
    writer.SetFileName("extracted_contour.vtp") # [cite: 7, 22]
    writer.SetInputData(polydata)
    writer.Write()
    print("Contour extraction complete. Saved as 'extracted_contour.vtp'")

if __name__ == "__main__":
    main()