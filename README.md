# chimp-data-parser

usage: 
* request & receive a zipfile from mailchimp of all your data: https://mailchimp.com/dsar-requests/
* unzip that zipfile into a directory
* copy chimp-data-parser.py into the top level of that directory  
e.g. when doing an ls on that directory, you should see something like this:  
`my-laptop$ ls -l`  
`drwxr-xr-x@ 96 my-user  staff  3072 Sep 23 14:37 c6ae6992-692e-47a1-b920-5d028600db62`  
`-rwxr-xr-x  01 my-user  staff  1845 Sep 23 14:41 chimp-data-parser.py`  
* execute chimp-data-parser.py at the cmd line from within that directory (e.g.: ./chimp-data-parser.py)
* you should now have a CSV file in that same directory, for example:  
`my-laptop$ ls -l`  
`drwxr-xr-x@ 96 my-user  staff    3072 Sep 23 14:37 c6ae6992-692e-47a1-b920-5d028600db62`  
`-rw-r--r--  01 my-user  staff  235226 Sep 23 14:43 c6ae6992-692e-47a1-b920-5d028600db62.csv`  
`-rwxr-xr-x  01 my-user  staff    2003 Sep 23 14:43 chimp-data-parser.py`  
that's it, that's how it works. The CSV should have all the data.
