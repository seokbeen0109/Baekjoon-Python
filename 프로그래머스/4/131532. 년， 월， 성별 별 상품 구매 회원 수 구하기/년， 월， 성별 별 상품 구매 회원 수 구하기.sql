-- 코드를 입력하세요
SELECT year(sales_date) as YEAR, month(sales_date) as MONTH, GENDER, count(distinct u.user_id) as USERS
from USER_INFO u
join ONLINE_SALE s on u.USER_ID=s.USER_ID
where gender is not null
group by year(sales_date), month(sales_date), gender
order by year(sales_date), month(sales_date), gender