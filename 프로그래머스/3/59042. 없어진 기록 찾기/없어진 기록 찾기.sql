-- 입양을 간 기록 O, 보호소에 들어온 기록 X
-- 동물 ID, 이름 조회
-- 동물 ID 정렬
SELECT o.animal_id, o.name
FROM animal_outs o
LEFT JOIN animal_ins i
ON i.animal_id = o.animal_id
WHERE i.animal_id IS NULL
ORDER BY animal_id