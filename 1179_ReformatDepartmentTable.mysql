/* SQL Schema:
Create table If Not Exists Department (id int, revenue int, month varchar(5))
Truncate table Department
insert into Department (id, revenue, month) values ('1', '8000', 'Jan')
insert into Department (id, revenue, month) values ('2', '9000', 'Jan')
insert into Department (id, revenue, month) values ('3', '10000', 'Feb')
insert into Department (id, revenue, month) values ('1', '7000', 'Feb')
insert into Department (id, revenue, month) values ('1', '6000', 'Mar')
*/

# Write your MySQL query statement below

select
    id,
    sum(if (month = "Jan", revenue, null)) as Jan_Revenue,
    sum(if (month = "Feb", revenue, null)) as Feb_Revenue,
    sum(if (month = "Mar", revenue, null)) as Mar_Revenue,
    sum(if (month = "Apr", revenue, null)) as Apr_Revenue,
    sum(if (month = "May", revenue, null)) as May_Revenue,
    sum(if (month = "Jun", revenue, null)) as Jun_Revenue,
    sum(if (month = "Jul", revenue, null)) as Jul_Revenue,
    sum(if (month = "Aug", revenue, null)) as Aug_Revenue,
    sum(if (month = "Sep", revenue, null)) as Sep_Revenue,
    sum(if (month = "Oct", revenue, null)) as Oct_Revenue,
    sum(if (month = "Nov", revenue, null)) as Nov_Revenue,
    sum(if (month = "Dec", revenue, null)) as Dec_Revenue
from
    Department
group by
    id
    
# Alternative solution

select
    ID.id as id,
    January.revenue as Jan_Revenue,
    February.revenue as Feb_Revenue,
    March.revenue as Mar_Revenue,
    April.revenue as Apr_Revenue,
    May.revenue as May_Revenue,
    June.revenue as Jun_Revenue,
    July.revenue as Jul_Revenue,
    August.revenue as Aug_Revenue,
    September.revenue as Sep_Revenue,
    October.revenue as Oct_Revenue,
    November.revenue as Nov_Revenue,
    December.revenue as Dec_Revenue
from
    (select distinct id from Department) as ID
left join Department as January on
    (ID.id = January.id and January.month = "Jan")
left join Department as February on
    (ID.id = February.id and February.month = "Feb")
left join Department as March on
    (ID.id = March.id and March.month = "Mar")
left join Department as April on
    (ID.id = April.id and April.month = "Apr")
left join Department as May on
    (ID.id = May.id and May.month = "May")
left join Department as June on
    (ID.id = June.id and June.month = "Jun")
left join Department as July on
    (ID.id = July.id and July.month = "Jul")
left join Department as August on
    (ID.id = August.id and August.month = "Aug")
left join Department as September on
    (ID.id = September.id and September.month = "Sep")
left join Department as October on
    (ID.id = October.id and October.month = "Oct")
left join Department as November on
    (ID.id = November.id and November.month = "Nov")
left join Department as December on
    (ID.id = December.id and December.month = "Dec")
group by
    id
