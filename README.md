# Airline_Project
Analytics Research & Implementation (MIS 40750)
Airline Programming Assignment


Team Members        Student Number    Contribution
Mark Doyle            13537123          Testing
Madhura Kashikar      16200240          Coding (count_seats, empy_seats_check)
Nicole McConville     12450428          Coding (seat_rows, max_seats, booking, refused_separated)


Implementatio:

Python and SQLite

Though this can also be implemented using other databases, only the care that will have to be taken is some parameters for connection and certain libraries will have to be imported.
We have used SQLite because the team has an understanding of sql and SQLite provides functionality for data to be imported from CSV files which makes slicing and dicing(data handling easy).

Assumptions: 

- The layout of the plane is consistent 
  - i.e. if the first row has 2 seats in either aisle (4 seats per row), then all rows are consistent in that layout
- Passengers are considered "separated" if for example a group of 4 is split into 2 in one row and 2 in another (TBC) 
- Can we update the database in one fell swoop at the end or can we make use of lists to do it all at once? (TBC)
  - the outline does say after each booking has been processed, update the separated/refused, so perhaps not 
  
Testing



  
  
