# https://adventofcode.com/2022/day/14


import time


points = set()
start = (500, 0)
floor = 0
end = False
count = 0


def parse(file):
    global points
    with open(file) as f:
        input = f.read().split('\n')
        input = [x.split(' -> ') for x in input]
        for line in input:
            i = 0
            while i < len(line) - 1:
                pt1 = eval((line[i]))
                pt2 = eval((line[i+1]))
                if pt1[0] == pt2[0]:
                    populate_vert(pt1, pt2)
                if pt1[1] == pt2[1]:
                    populate_horiz(pt1, pt2)
                i +=1

 
def get_floor():
    global floor
    floor = max(points, key=lambda x: x[1])[1]

 
def populate_horiz(pt1, pt2):
    if pt1[0] > pt2[0]:
       for i in range(pt1[0], pt2[0]-1, -1):
            points.add((i, pt1[1]))
    else:
        for i in range(pt1[0], pt2[0]+1):
            points.add((i, pt1[1]))


def populate_vert(pt1, pt2):
    if pt1[1] > pt2[1]:
        for i in range(pt1[1], pt2[1]-1, -1):
         points.add((pt1[0], i))
    else:
        for i in range(pt1[1], pt2[1]+1):
            points.add((pt1[0], i))


def drop_sand(pt):
    global count
    global end
    while (pt[0], pt[1]) not in points:
        if pt[1] >= floor:
            end = True
            break
        if (pt[0], pt[1]+1) not in points:
            pt = (pt[0], pt[1]+1)
        elif (pt[0]-1, pt[1]+1) not in points:
            pt = (pt[0]-1, pt[1]+1)
        elif (pt[0]+1, pt[1]+1) not in points:
            pt = (pt[0]+1, pt[1]+1)
        else:
            points.add(pt)
            count += 1
            break

    
if __name__ == '__main__':
    start_time = time.time()

    #file = 'puzzle_test_inputs.txt'
    file = 'puzzle_inputs.txt'
    parse(file)
    get_floor()
    while not end:
        drop_sand(start)
    print(count) # 24, 745

    print(f"--- {time.time() - start_time} seconds ---")