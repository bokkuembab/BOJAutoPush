-- 2022년 1월, 카테고리 별 도서 판매량 합산
-- 카테고리, 총 판매량 조회
-- 카테고리 오름차순 정렬
SELECT b.category, SUM(bs.sales) total_sales
FROM book_sales bs
JOIN book b
    ON bs.book_id = b.book_id
WHERE DATE_FORMAT(bs.sales_date, "%Y-%m") = '2022-01'
GROUP BY b.category
ORDER BY b.category