-- 보호 시작일 > 입양일 동물
-- ID, NAME 조회
-- 보호 시작일 정렬
SELECT i.animal_id, i.name
FROM animal_ins i
JOIN animal_outs o
ON i.animal_id = o.animal_id
WHERE i.datetime > o.datetime
ORDER BY i.datetime