# SW-P-08-General-Remote-Protocol
SW-P-08  Broadcast Protocol Implementation 

## Command Table

| Command                        | Command Bytes | Description                                                                                                                         
|--------------------------------|---------------|
| Extended Interrogate           | 129           | Where Levels are greater than 16, and Destinations are greater than 1024.                                                           
| Crosspoint Connect 02          | 02            | Where Levels are less than or equal to 16, Sources are less than or equal to 1024, and Destinations are less than or equal to 1024. 
| Extended Crosspoint Connect    | 129           | Where Levels are greater than 16 or Sources are greater than 1024, or Destinations are greater than 1024.                              
| All Source Names Request       | 100           | User selectable choice of 4, 8, or 12 character labels.                                   
