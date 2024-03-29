-- 코드를 입력하세요
WITH JOINED_2021 AS(
SELECT
    COUNT(*) AS CNT
FROM
    USER_INFO
WHERE
    YEAR(JOINED) = 2021
)
SELECT
    YEAR(OS.SALES_DATE) AS YEAR,
    MONTH(OS.SALES_DATE) AS MONTH,
    COUNT(DISTINCT OS.USER_ID) AS PURCHASED_USERS,
    ROUND(COUNT(DISTINCT OS.USER_ID) / J2.CNT, 1) AS PURCHASED_RATIO
FROM
    ONLINE_SALE AS OS
        INNER JOIN
    USER_INFO AS UI ON OS.USER_ID = UI.USER_ID,
    JOINED_2021 AS J2
WHERE
    YEAR(UI.JOINED) = 2021
GROUP BY
    YEAR(OS.SALES_DATE),
    MONTH(OS.SALES_DATE)
ORDER BY
    1 ASC,
    2 ASC