import base64
image = open('EncodedFile.b64', 'rb')
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
image_64_decode = base64.decodestring(image_64_encode) 
image_result = open('dec.pdf', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)
