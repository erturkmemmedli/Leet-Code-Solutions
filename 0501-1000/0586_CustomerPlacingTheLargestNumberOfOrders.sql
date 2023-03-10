/* SQL Schema:
Create table If Not Exists orders (order_number int, customer_number int)
Truncate table orders
insert into orders (order_number, customer_number) values ('1', '1')
insert into orders (order_number, customer_number) values ('2', '2')
insert into orders (order_number, customer_number) values ('3', '3')
insert into orders (order_number, customer_number) values ('4', '3')
*/

# Write your MySQL query statement below

select
    customer_number
    from orders
    group by customer_number
    order by count(order_number) desc
    limit 1

# Alternative solution

with counter as (select customer_number, count(order_number) as cnt from orders group by customer_number)
select customer_number from counter where cnt = (select max(cnt) from counter)
