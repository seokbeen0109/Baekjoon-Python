-- 코드를 입력하세요
SELECT b.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, sum(s.sales*b.price) as TOTAL_SALES
from BOOK b
join AUTHOR a on b.AUTHOR_ID=a.AUTHOR_ID
join BOOK_SALES s on b.BOOK_ID=s.BOOK_ID
where s.sales_date between '2022-01-01' and '2022-01-31'
group by b.AUTHOR_ID, b.category
order by b.AUTHOR_ID, b.category desc