# SW-P-08-General-Remote-Protocol
SW-P-08  Broadcast Protocol Implementation 

## Command Table
### Command                         
#### 1. Extended Interrogate           
Command Bytes : 129           
Description : Where Levels are greater than 16, and Destinations are greater than 1024.                                                           
#### 2. Crosspoint Connect 
Command Bytes :02                      
Description: Where Levels are less than or equal to 16, Sources are less than or equal to 1024, and Destinations are less than or equal to 1024. 
#### 3. Extended Crosspoint Connect    
Command Bytes: 129           
Description: Where Levels are greater than 16 or Sources are greater than 1024, or Destinations are greater than 1024.                              
#### 4. All Source Names Request      
Command Bytes: 100      
Description: User selectable choice of 4, 8, or 12 character labels.                                   
