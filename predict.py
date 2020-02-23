def prediction():
	#load image
    from keras.preprocessing.image import ImageDataGenerator
    test_datagen = ImageDataGenerator(rescale = 1./255)
    test_data = test_datagen.flow_from_directory('images/',target_size = (64, 64),batch_size = 32,class_mode = 'binary')
    #load ml model
    import pickle
    model = pickle.load(open('model.sav', 'rb'))
    pred = model.predict(test_data)
    #convert float to binary
    pred = pred>0.5
    # True == Dog & False == Cat
    return pred