-- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID, 이름 조회
-- ID 순으로 조회
SELECT ao.ANIMAL_ID, ao.NAME FROM ANIMAL_OUTS ao
LEFT JOIN ANIMAL_INS ai ON ao.ANIMAL_ID=ai.ANIMAL_ID
WHERE ai.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID;
