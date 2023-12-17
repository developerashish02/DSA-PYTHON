class Camera:
    def __init__(self, camera):
        self.camera = camera

    # update method
    def update_camera(self, updated_camera):
        self.camera = updated_camera


# creating the object using class

camera_obj = Camera("oppo 37")
camera_obj.update_camera("Poco x2")

print(camera_obj.camera)
