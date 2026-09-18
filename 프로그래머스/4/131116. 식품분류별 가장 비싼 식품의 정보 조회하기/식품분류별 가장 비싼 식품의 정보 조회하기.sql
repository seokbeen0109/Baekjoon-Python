-- 코드를 입력하세요
SELECT CATEGORY, price as MAX_PRICE, PRODUCT_NAME
from (select CATEGORY, price, PRODUCT_NAME, rank() over (partition by category order by price desc) as rnk from FOOD_PRODUCT where CATEGORY in ('과자','국','김치','식용유')) T
where rnk=1
order by price desc