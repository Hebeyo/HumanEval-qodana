def triangle_area(a, b, c):
    # Your code here
    # use the if statement to check if the three sides form a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        # if not, return -1
        return -1
    # if yes, use Heron's formula to calculate the area of the triangle
    s = (a + b + c)/2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    # round the area to 2 decimal points
    area = round(area, 2)
    return area
