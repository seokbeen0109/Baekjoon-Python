-- 코드를 작성해주세요
select i.ITEM_ID, i.ITEM_NAME, i.RARITY
from ITEM_INFO i
join ITEM_TREE t on i.ITEM_ID=t.ITEM_ID
join item_info p on t.PARENT_ITEM_ID=p.ITEM_ID
where p.rarity='rare'
order by ITEM_ID desc