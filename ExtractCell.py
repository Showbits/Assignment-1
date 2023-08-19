## This program shows how to load a VTK Image data with extension *.vti and then
## how to access the cell data, extract one cell from the list of cells,
## access data values at each cell corner and then store the cell into a 
## vtkpolydata file format.
#################################################################################

## Import VTK
from vtk import *

## Load data
#######################################
reader = vtkXMLImageDataReader()
reader.SetFileName('Data/Isabel_2D.vti')
reader.Update()
data = reader.GetOutput()

## Query how many cells the dataset has
#######################################
numCells = data.GetNumberOfCells()

## Get a single cell from the list of cells
###########################################
 ## cell index = 0

## Query the 4 corner points of the cell
#########################################
pid1 = cell.GetPointId(0)
pid2 = cell.GetPointId(1)
pid3 = cell.GetPointId(3)
pid4 = cell.GetPointId(2)

## Print the 1D indices of the corner points
############################################
print('1D indices of the cell corner points:')
print(pid1,pid2,pid3,pid4) ## in counter-clockwise order


## Get values at each vertex
## First Get the array
dataArr = data.GetPointData().GetArray('Pressure') # Extracting out the pressure array from our data
val1 = dataArr.GetTuple1(pid1) # Finding the value of the pressure at point pid1
val2 = dataArr.GetTuple1(pid2)
val3 = dataArr.GetTuple1(pid3)
val4 = dataArr.GetTuple1(pid4)
#print(val1,val2,val3,val4)

## Print the locations (3D coordinates) of the points
#######################################################
print('Point locations of cell corners in counter clockwise order and their data values:')
print(data.GetPoint(pid1),val1) # Printing the position of the corner points of our cell
print(data.GetPoint(pid2),val2)
print(data.GetPoint(pid3),val3)
print(data.GetPoint(pid4),val4)


## Extract and store one cell
#############################
points = vtkPoints() # making points object
points.InsertNextPoint(data.GetPoint(pid1)) # adding pid1 coordinates in points object
points.InsertNextPoint(data.GetPoint(pid2))
points.InsertNextPoint(data.GetPoint(pid3))
points.InsertNextPoint(data.GetPoint(pid4))

## The Data Array for holding data values
#########################################
dataArray = vtkFloatArray() # Made an array
dataArray.SetName('Pressure') # Set name pressure of that array
dataArray.InsertNextTuple1(val1) # Inserting pressure of one corner of the cell in dataArray
dataArray.InsertNextTuple1(val2)
dataArray.InsertNextTuple1(val3)
dataArray.InsertNextTuple1(val4)

## Create the cell, which is a polyline
#########################################
polyLine = vtkPolyLine() # Creating polyline object
polyLine.GetPointIds().SetNumberOfIds(5) # Creating ids of each point which is there in polyline  
polyLine.GetPointIds().SetId(0, 0)
polyLine.GetPointIds().SetId(1, 1)
polyLine.GetPointIds().SetId(2, 2)
polyLine.GetPointIds().SetId(3, 3)
polyLine.GetPointIds().SetId(4, 0)

### Create a polydata
######################
pdata = vtkPolyData() # creating polyData object

### Create a cell array to store the polyline
#############################################
cells = vtkCellArray() # created cell array
cells.InsertNextCell(polyLine) # Inserted the cell in the cells array

### Add points and cells to polydata
####################################
pdata.SetPoints(points) # Inserting points in our polyData
pdata.SetLines(cells) # Inserting cell in our polyData
pdata.GetPointData().AddArray(dataArray) # Inserting pressure values in our polyData


### Store the polydata into a vtkpolydata file with extension .vtp
####################################################################
writer = vtkXMLPolyDataWriter() # Poly Data writer
writer.SetInputData(pdata) # Inputting data in our writer
writer.SetFileName('onecell.vtp') # Setting file name
writer.Write() # Writing polyData back
