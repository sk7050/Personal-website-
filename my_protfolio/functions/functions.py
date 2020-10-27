def Upload_File(f):
    with open('D:/Google Driver/Education/Paython/test_project/my_test_project/media','wb+') as destination:
        for chunk in f.chunks():  
            destination.write(chunk)
