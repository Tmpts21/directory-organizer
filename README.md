
## Organize and manage messy directories 🧹

the script runs with a json file. Inside the json file you can specify the configurations to organize the directory.

```
# config.json

{   
"directory" : 
	{
		"path": ["path of directory to organize ex: C:\\Users\\tmpts21\\Desktop"]
	},

"automate" : [ 
		{ 
			"type" : "IMAGES" ,  
			"organize" : "True" ,    
			"file_ext" :".jpeg .jpg .gif .png .PNG .JPG "      
		},   
		{
			
			"type" : "DOCS" , 
			"organize" : "True" ,   
			"file_ext" : ".docx .pdf .doc"    
		}, 
		{
			"type" : "VIDEOS" ,  
			"organize" : "True" ,  
			"file_ext" : ".wmv .mov .mp4 .mpg .mpeg .mkv" 
		}
	] 
}

```
You can add more type of files you want by editing this config file. Lets say i also want music files to be cleaned and reorganized into another folder.

I'll just add this block of key value pairs inside the "automate" key in the json config file 

```
	{
		"type" : "music" ,  
		"organize" : "True" ,  
		"file_ext" : ".mp3 .flac .wav " 
	}

```

You can also organize multiple directories at once 

```
"directory" : [ 
	{
		"path": ["C:\\Users\\tmpts21\\Desktop" , "C:\\Users\\tmpts21\\Downloads" ]
	} 
],

```

After running the script you will notice new folders containing all the files organized. 

```
"C:\\YourPathSpecifed\\{TYPE} 

Ex : "C:\\Users\\tmpts21\\Desktop\\IMAGES" | "C:\\Users\\tmpts21\\Desktop\\DOCS"

```






