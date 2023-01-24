/* SQL Schema:
Create table If Not Exists Employee (id int, name varchar(255), salary int, managerId int)
Truncate table Employee
insert into Employee (id, name, salary, managerId) values ('1', 'Joe', '70000', '3')
insert into Employee (id, name, salary, managerId) values ('2', 'Henry', '80000', '4')
insert into Employee (id, name, salary, managerId) values ('3', 'Sam', '60000', 'None')
insert into Employee (id, name, salary, managerId) values ('4', 'Max', '90000', 'None')
*/

# Write your MySQL query statement below

select name as Employee from Employee e where salary > (select salary from Employee where e.managerId = id)

# Alternative solution

select a.name as Employee
    from Employee a
    left join Employee b
    on a.managerId = b.id
    where a.salary > b.salary
    
# Alternative solution

select a.name as Employee
    from Employee a, Employee b
    where a.managerId = b.id and a.salary > b.salary
