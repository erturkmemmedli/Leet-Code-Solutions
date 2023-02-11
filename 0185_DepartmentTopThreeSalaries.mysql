/* SQL Schema:
Create table If Not Exists Employee (id int, name varchar(255), salary int, departmentId int)
Create table If Not Exists Department (id int, name varchar(255))
Truncate table Employee
insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '85000', '1')
insert into Employee (id, name, salary, departmentId) values ('2', 'Henry', '80000', '2')
insert into Employee (id, name, salary, departmentId) values ('3', 'Sam', '60000', '2')
insert into Employee (id, name, salary, departmentId) values ('4', 'Max', '90000', '1')
insert into Employee (id, name, salary, departmentId) values ('5', 'Janet', '69000', '1')
insert into Employee (id, name, salary, departmentId) values ('6', 'Randy', '85000', '1')
insert into Employee (id, name, salary, departmentId) values ('7', 'Will', '70000', '1')
Truncate table Department
insert into Department (id, name) values ('1', 'IT')
insert into Department (id, name) values ('2', 'Sales')
*/

# Write your MySQL query statement below

select
    d.name as Department,
    e.name as Employee,
    e.salary as Salary
from
    Department d,
    Employee e,
    Employee e2
where
    e.departmentId = d.id and
    e.departmentId = e2.departmentId and
    e.salary <= e2.salary
group by
    d.id, e.name
having
    count(distinct e2.salary) <= 3
order by
    d.name asc,
    e.salary desc
