# SQL Introduction Scripts

This directory contains SQL scripts to manage databases and tables for the database `hbtn_0c_0`. Below is a description of each file:

| File Name                         | Description                                                  |
|-----------------------------------|--------------------------------------------------------------|
| 0-list_databases.sql              | Lists all databases in the MySQL server.                     |
| 1-create_database_if_missing.sql  | Creates a database if it does not already exist.             |
| 2-remove_database.sql             | Deletes a database if it exists.                             |
| 3-list_tables.sql                 | Lists all tables in the selected database.                   |
| 4-first_table.sql                 | Creates the `first_table` with `id` and `name`.         |
| 5-full_table.sql                  | Shows the full description of `first_table`.               |
| 6-list_values.sql                 | Lists all rows in the `first_table`.                       |
| 7-insert_value.sql                | Inserts a new row into the `first_table`.                  |
| 8-count_89.sql                    | Counts rows in `first_table` where `id = 89`.            |
| 9-full_creation.sql               | Creates `second_table` and populates it with data.         |
| 10-top_score.sql                  | Lists rows in `second_table` ordered by score (desc).      |
| 11-best_score.sql                 | Lists rows in `second_table` with score >= 10 (desc).      |
| 12-no_cheating.sql                | Updates Bob's score to 10 without using the `id`.          |
| 13-change_class.sql               | Deletes rows with score <= 5 from `second_table`.          |
| 14-avg_score.sql                  | Calculates the average score from `second_table`.          |
| 15-max_score.sql                 | Finds the highest score in `second_table`.                 |
| 16-no_link.sql                   | Lists rows in `second_table` with valid names, ordered by score (desc). |

## How to Use
1. Place the  files in your working directory.
2. Run the files in sequence using the MySQL client.

