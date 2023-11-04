-- ANIMAL_INS 테이블에 등록된 모든 레코드에 대해, 각 동물의 아이디, 이름, 들어온 날짜 조회
-- 아이디 순으로 정렬
SELECT animal_id, name, DATE_FORMAT(datetime,"%Y-%m-%d") '날짜'
FROM animal_ins
ORDER BY animal_id