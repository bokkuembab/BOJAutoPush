-- 보호소에 들어올 때 중성화 x, 나갈 때 중성화 o
-- ID, ANIMAL_TYPE, NAME
-- ID 정렬
SELECT i.animal_id, i.animal_type, i.name
FROM animal_ins i
JOIN animal_outs o
ON i.animal_id = o.animal_id
WHERE i.sex_upon_intake LIKE 'Intact%' AND o.sex_upon_outcome NOT LIKE 'Intact%'
ORDER BY i.animal_id