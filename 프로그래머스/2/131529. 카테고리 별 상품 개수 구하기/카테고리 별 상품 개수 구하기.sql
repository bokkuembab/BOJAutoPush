-- 상품 카테고리 코드(product_code 앞 두자리) 별 상품 개수
-- 카테고리 오름차순 정렬
SELECT LEFT(product_code, 2) category, COUNT(*) products
FROM product
GROUP BY category
ORDER BY category