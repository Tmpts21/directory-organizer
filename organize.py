from json import load
import os  
from datetime import datetime 

def move(file_ext , directories , _type , sort = None) :               

    for directory in directories :  
        files = os.listdir(directory)      
        for file in files :            
            if os.path.splitext(file)[1] in file_ext.split():
                if not os.path.exists(os.path.join(directory, _type,)) : #check if folder exists
                    os.mkdir(os.path.join(directory , _type))   #move file to {/dir/type/file} 
                From =  f"{directory}/{file}"  
                To = f"{directory}/{_type}/{file}" 
                try :  
                    os.rename(From , To )   
                except FileExistsError :     
                    os.rename(From , To + datetime.now() )     

# run the script
def run_script(config) :                    
    try : 
        for i in config["automate"] :           
            if i["organize"] == "True" :              
                move ( i["file_ext"], config['directory']['path'] , i["type"] )             
   
    except FileNotFoundError as err :       
        return err 
        


def main() :   
    # read config file  
    with open("./config.json" , 'r' ) as conf : 
        config = load(conf)    

    run_script(config)


if __name__ == "__main__":   
    main() 



