from google.appengine.api import images

def thumbnailify(blob_key):
    if blob_key:
        img = img = images.Image(blob_key=blob_key)
        img.resize(width=100, height=100)
        img.im_feeling_lucky()
        
        return img.execute_transforms(output_encoding=images.JPEG)
        
def adjustContrast(blob_key):
    if blob_key:
        img = images.Image(blob_key=blob_key)
        img.im_feeling_lucky()
        
        return img.execute_transforms(output_encoding=images.JPEG)
    