-- 코드를 입력하세요
SELECT b.CATEGORY, sum(s.sales) as TOTAL_SALES
from BOOK b
join BOOK_SALES s on b.BOOK_ID=s.BOOK_ID
where s.sales_date like '2022-01%'
group by b.category
order by b.category