import os

def arrange_files(files, ext):
    files_with_ext = [file for file in files if file.endswith(ext)]  # This lists directories which are having .jpg extension.
    # print(files_with_ext)

    # This "if not exists"  ensures to create the images folder in the parent directory if it does not exists.
    if not(os.path.exists("07_BULK_RENAME/images")):
        os.mkdir("07_BULK_RENAME/images")


    # # This is the initial approach we took :
    # i = 1
    # for file in files_with_ext:
    #     os.rename(file, f"photo:{i}{ext}")
    #     i+=1 


    # This approach is much preferred compared to the approach above using enumerate function:   
    for i, file in enumerate(files_with_ext):
        
        # Create the correct relative path to the source file
        source_path = os.path.join("07_BULK_RENAME", file)
        
        # Rename and move the file
        os.rename(source_path, f"07_BULK_RENAME/images/my_photo - {i+1}{ext}")


if __name__=="__main__":
    files = os.listdir("07_BULK_RENAME")
    arrange_files(files, ".jpg")