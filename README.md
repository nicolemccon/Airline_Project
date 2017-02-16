# Airline_Project
Analytics Research & Implementation (MIS 40750) - Airline Programming Assignment



| Team Members  | Student Number| Contribution  |
| :-------------: |:-------------:| :-------------:|
| Mark Doyle    | 13537123 | Testing & Test Document |
| Madhura Kashikar      | 16200240      |   Coding (count_seats, empty_seats_check) |
| Nicole McConville | 12450428      |    Coding (seat_rows, max_seats, booking, refused_separated) & README |

## Program Use

This program is used as a booking system for a plane contained on a database file where the booking information is contained in a csv file.  


## Instructions 

In order to successfully run the program from the command line, enter the following: 

``` python 
> python seat_assign_12450428_13537123_16200240.py airline_seating.db bookings.csv

```

Where:
- seat_assign_12450428_13537123_16200240.py is the Python program
- airline_seating.db is the database representing the plane
- bookings.csv is the csv file containing the flight bookings broken down by name and the number of seats booked per name

## Program Function

The program is fully commented, however a brief description of how the program functions is outlined below. 

- The connection is made to the database by utilising the argument sys.argv[1] from the command line.
- The metrics for the number of available seats and the number of rows on the plane are calculated.
- The booking function then reads in the csv file, sys.argv[2], as specified in the command line.
  - The function reads the csv file line by line and checks each booking individually.
  - If the number of passengers in the booking are less than or equal to the number of available seats, the function will proceed with the booking, otherwise the passengers_refused metric will be updated accordingly. 
  - If the function does proceed with the booking, the seat allocation is processed through one of the following paths: 
    1. 
    2. 

## Implementation

### Languages 

For the purpose of carrying out this assignment, Python 3.5.2 and SQLite 3.15.2 were used. 

### Libraries 

The following libraries were imported and used within our Python program:
- sqlite3
  - Used to create the connection between the Python file and the SQL database. 
- csv
  - Used to read in the csv file containing the passenger names and number of seats per booking 
- sys
  - Used to allow multiple arguments to be read in when running the code directly from the command line
  - For the purpose of this program, sys.argv[1] is specified to be the database file, and sys.argv[2] is the csv file. 

## Assumptions 

This program was built based on the following assumptions:

### Layout

The layout of the plane is consistent from front to back. In other words, for example, if the plane has 4 seats per row at the front of the plane, that this layout is consistent throughout, meaning that there are also 4 seats per row at the back of the plane. 

### Separation Understanding 

"...a number representing how many passengers are seated away from any other member of their party"

For the purpose of the separation metric, our interpretation of the above statement was that if a booking has to be separated in any way, then the total number of passengers on that booking will be included in the metric. For example, if a group of 5 making a booking on a plane which seats 4 people per row, then the 5 passengers will be included in the separation metric due to the fact that they are sitting away from at least one member of their party. 

## Testing
The testing carried out has been covered in the separate document entitled "Airline Testing" (TBC).



  
  
