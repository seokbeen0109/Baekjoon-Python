-- 코드를 입력하세요
SELECT f.FLAVOR
from FIRST_HALF f
join JULY j on f.flavor=j.flavor
group by f.FLAVOR
order by sum(j.TOTAL_ORDER)+f.TOTAL_ORDER desc
limit 3
