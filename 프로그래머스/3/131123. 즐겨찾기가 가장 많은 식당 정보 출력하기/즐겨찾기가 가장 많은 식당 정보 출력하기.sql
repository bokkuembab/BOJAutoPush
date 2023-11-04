-- 음식종류별, 즐겨찾기수가 가장 많은 식당
-- 음식 종류, ID, 식당 이름, 즐겨찾기수
-- 음식종류 내림차순 정렬
SELECT food_type, rest_id, rest_name, favorites
FROM rest_info
WHERE (food_type, favorites) 
    IN (SELECT food_type, MAX(favorites) 
        FROM rest_info
        GROUP BY food_type)
ORDER BY food_type DESC