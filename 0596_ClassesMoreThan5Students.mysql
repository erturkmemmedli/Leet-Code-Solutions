/*SQL Schema:
Create table If Not Exists Courses (student varchar(255), class varchar(255))
Truncate table Courses
insert into Courses (student, class) values ('A', 'Math')
insert into Courses (student, class) values ('B', 'English')
insert into Courses (student, class) values ('C', 'Math')
insert into Courses (student, class) values ('D', 'Biology')
insert into Courses (student, class) values ('E', 'Math')
insert into Courses (student, class) values ('F', 'Computer')
insert into Courses (student, class) values ('G', 'Math')
insert into Courses (student, class) values ('H', 'Math')
insert into Courses (student, class) values ('I', 'Math')
*/

# Write your MySQL query statement below

select class from
    (
        select class, count(class) as count
        from Courses
        group by class
    ) as _
where count >= 5

# Alternative solution

with cte as (select class, count(class) as c from Courses group by class)
select class from cte where c >= 5
