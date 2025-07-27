def get_size(w,h,d):
    side1 = w * h
    side2 = h * d
    side3 = w * d

    surface_area = 2 * (side1 + side2 + side3)

    volume = w * h * d

    return [surface_area, volume]
