# Library Management System - SQL Queries

-This project contains SQL queries for creating and managing a **Library Management System**.
-The provided SQL script includes queries for setting up the database, inserting sample data, and running various data analysis queries to manage and track books, authors, members, and checkouts.

## **Tables Included:**

1. **Books**: Stores information about books, including title, author, genre, and publish year.
2. **Authors**: Stores details about authors, including their name and country of origin.
3. **Members**: Contains information about library members such as name, membership type, and contact details.
4. **Checkouts**: Tracks book checkouts, including member ID, book ID, checkout date, and return status.
5. **Returns**: Records the return dates of books and any associated late fees.

## **Key Features:**

- **SQL Queries for Creating Tables**: Includes queries to create the necessary tables for the library management system.
- **Data Insertion Queries**: Sample data insertion for each table, including books, authors, members, checkouts, and returns.
- **Analysis Queries**:
  - Track the number of books checked out by each member.
  - Identify the most popular books based on checkout counts.
  - Identify overdue books.
  - Calculate the average checkout duration for each book.
- **Export Query**: Includes an example query (`INTO OUTFILE`) for exporting data, such as the most popular books, to a CSV file (if using MySQL).


