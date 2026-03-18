
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort(reverse=True)
    blueShirtSpeeds.sort(reverse=True)
    total_speeds = 0
    for idx in range(len(redShirtSpeeds)):
        if not fastest:    
            c_speed = max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
        else:
            reverse_idx = (len(redShirtSpeeds) - 1) - idx
            if redShirtSpeeds[0] < blueShirtSpeeds[0]:
                c_speed = max(redShirtSpeeds[reverse_idx], blueShirtSpeeds[idx])
            else:
                c_speed = max(redShirtSpeeds[idx], blueShirtSpeeds[reverse_idx])
        total_speeds += c_speed
    return total_speeds
