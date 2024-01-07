# MySQL Replication Setup

This project focuses on setting up MySQL replication between two servers, web-01 and web-02. MySQL replication involves maintaining a copy of a MySQL server's data on another server, known as the replica.

## Tasks

### 1. Install MySQL (Task 0)
Ensure MySQL 5.7.x is installed on both web-01 and web-02 servers.

### 2. Create MySQL User (Task 1)
Create a MySQL user named `holberton_user` on both servers with specific permissions, allowing external access for checking replication status.

### 3. Create Database and Table (Task 2)
Set up a database named `tyrell_corp` on the primary server (web-01) with a table named `nexus6` containing at least one entry. Grant `holberton_user` SELECT permissions on the table.

### 4. Create Replica User (Task 3)
On the primary server (web-01), create a new user named `replica_user` with replication permissions. Verify the creation of `replica_user` using `holberton_user` and SELECT privileges on the `mysql.user` table.

### 5. Setup Primary-Replica Infrastructure (Task 4)
Configure MySQL replication infrastructure with web-01 as the primary server and web-02 as the replica. The primary MySQL server should have the database `tyrell_corp`. Provide configuration files for both the primary and replica servers.

## Ultimate Goal
The ultimate goal is to achieve a functional MySQL replication setup, providing redundancy and load distribution for the database. This setup allows for improved reliability by having a copy of the data on the replica server and enables distributing read operations between the primary and replica servers, improving query response speed.
