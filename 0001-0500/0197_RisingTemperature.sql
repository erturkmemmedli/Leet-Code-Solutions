/* SQL Schema:
Create table If Not Exists Weather (id int, recordDate date, temperature int)
Truncate table Weather
insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10')
insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25')
insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20')
insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30')
*/

# Write your MySQL query statement below

select a.id
    from Weather a
    join Weather b
    where a.temperature > b.temperature and datediff(a.recordDate, b.recordDate) = 1
    
# Alternative solution

select a.id from Weather a, Weather b where a.temperature > b.temperature and datediff(a.recordDate, b.recordDate) = 1
