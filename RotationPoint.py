
# Given a list that is rotated or not rotated but sorted,
# if the list is rotated, findRotationPoint(rotated_list) returns the rotation point; 
# if the list is not rotated but sorted, print "List is not rotated"
# Given a sorted list of size n, a rotated list is constructed by picking an index (rotation point)
# r and move the list portion [r,n-1] before the list portion [0, r-1]
def findRotationPoint(rotated_list):

	first_int = rotated_list[0]
	floor = 0 
	ceiling = len(rotated_list) - 1

	while (floor <= ceiling):

		mid = floor + (ceiling - floor) / 2

		if (rotated_list[mid] >= first_int):
			floor = mid + 1
		elif (rotated_list[mid] < first_int):
			ceiling = mid - 1

	check = len(rotated_list)


	if (floor == check): # list not rotated
		print "List is not rotated"
	else:
		print "Rotation point = " + str(floor)

# test code
rotated_list = [600,700,800,900,1000,100,200]
findRotationPoint(rotated_list)
# output: Rotation point = 5

rotated_list = [600,100,200,300,400,500]
findRotationPoint(rotated_list)
# output: Rotation point = 1

rotated_list = [100,200,300,400,500,600,700]
findRotationPoint(rotated_list)
# output: List is not rotated

rotated_list = [600,700,100,200,300,400,500,600,1000,2000]
findRotationPoint(rotated_list)
# output: Rotation point = 2
