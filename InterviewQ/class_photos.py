def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[0] < blueShirtHeights[0]:
        front_row = redShirtHeights
        back_row = blueShirtHeights
    else:
        front_row = blueShirtHeights
        back_row = redShirtHeights  
    
    for idx in range(len(front_row)):
        if front_row[idx] >= back_row[idx]:
            return False
    return True
