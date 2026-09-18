-- 코드를 입력하세요
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, sum(o.amount)*p.price as TOTAL_SALES
from FOOD_PRODUCT p
join FOOD_ORDER o on p.PRODUCT_ID=o.PRODUCT_ID
where o.PRODUCE_DATE between '2022-05-01' and '2022-05-31'
group by o.product_id
order by TOTAL_SALES desc, p.PRODUCT_ID