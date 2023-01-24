/* SQL Schema:
Create table If Not Exists Person (Id int, Email varchar(255))
Truncate table Person
insert into Person (id, email) values ('1', 'john@example.com')
insert into Person (id, email) values ('2', 'bob@example.com')
insert into Person (id, email) values ('3', 'john@example.com')
*/

# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

delete a from Person a, Person b where a.id > b.id and a.email = b.email
