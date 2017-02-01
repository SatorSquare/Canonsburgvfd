from google.appengine.api import images

def thumbnailify(photo):
    if photo:
        img = images.Image(photo)
        img.resize(width=80, height=100)
        img.im_feeling_lucky()
        thumbnail = img.execute_transforms(output_encoding=images.JPEG)
        
        self.response.headers['Content-Type'] = 'image/jpeg'
        self.response.out.write(thumbnail)
        return thumbnail
        
def adjustContrast(photo):
    if photo:
        img = images.Image(photo)
        img.im_feeling_lucky()
        return img.execute_transforms(output_encoding=images.JPEG)
    