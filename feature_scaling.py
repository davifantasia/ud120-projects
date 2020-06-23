def featureScaling(arr):
    x_max = max(arr)
    x_min = min(arr)
    scaled_features = [(x - x_min) / float(x_max - x_min) for x in arr]
    return scaled_features


# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)