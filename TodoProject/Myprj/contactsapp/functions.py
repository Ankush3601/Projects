def handle_fileupload(fn):
    with open("contactsapp/static/uploads/"+fn.name,"wb+")as dst:
        for chunk in fn.chunks():
            dst.write(chunk)