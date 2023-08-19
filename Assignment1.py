##Import VTK
from vtk import *


##Load data

reader = vtkXMLImageDataReader() 
reader.SetFileName('Data/Isabel_2D.vti') 
reader.Update() 
data = reader.GetOutput()

##No. of cells in the dataset

numcells = data.GetNumberOfCells()
print(numcells)

##Dimension of the dataSet
dim = data.GetDimensions()
print(dim)

##No Of Points
numpoints = data.GetNumberOfPoints()
print(numpoints)

##Range of Pressure

range = data.GetPointData().GetArray('Pressure').GetRange()
print(range)


##Average of Pressure

dataArr = data.GetPointData().GetArray('Pressure')
sum = 0

for i in range(numpoints):
    print(3)

##for i in range(numpoints):
##    sum = sum + dataArr.GetTuple1(i)
##print(sum/numpoints)

#print(dataArr)


#cell 0

index = 0
cell = data.GetCell(index)
pid1 = cell.GetPointId(0)
pid2 = cell.GetPointId(1)
pid3 = cell.GetPointId(3)
pid4 = cell.GetPointId(2)

#printing the indices of four corner

print(pid1,pid2,pid3,pid4)


#3D Coordinates

print(data.GetPoint(pid1))
print(data.GetPoint(pid2))
print(data.GetPoint(pid3))
print(data.GetPoint(pid4))



