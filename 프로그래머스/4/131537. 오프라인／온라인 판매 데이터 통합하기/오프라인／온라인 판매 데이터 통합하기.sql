SELECT DATE_FORMAT(z.sales_date, "%Y-%m-%d") sales_date, 
        z.product_id, z.user_id, z.sales_amount
FROM (
    SELECT user_id, sales_date, product_id, sales_amount
    FROM online_sale
    UNION ALL
    SELECT NULL, sales_date, product_id, sales_amount
    FROM offline_sale
    ) z
WHERE sales_date LIKE "2022-03%"
ORDER BY sales_date, product_id, user_id