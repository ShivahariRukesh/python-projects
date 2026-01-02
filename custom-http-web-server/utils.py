import pathlib

# creating the index html file if it doesn't exist
def create_index_html_file():

        try:
            items = list( pathlib.Path.iterdir(pathlib.Path(str(pathlib.Path.cwd()))))
            files_only =[i for i in items if i.is_file()]
            show=[]
            if( not 'index.html' in (show:=[s[-1] for s in [str(f).split('/') for f in files_only]]) ):
                    with open("index.html",'w') as f:
                        content_file = open("html-content.txt",'r')
                        for content_line in content_file:
                            f.write(content_line)

        except Exception as err:
            print("Error while creating the index html file")



if __name__ =="__main__":
    create_index_html_file()