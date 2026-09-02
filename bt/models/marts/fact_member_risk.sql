{{ config(materialized='table', tags=['risk_analytics']) }}

WITH transactions AS (
    SELECT * FROM {{ ref('stg_transactions') }}
)

SELECT 
    member_id,
    transaction_date,
    amount,
    -- Core feature for Dave's ExtraCash Overdraft Risk Model
    SUM(amount) OVER (
        PARTITION BY member_id 
        ORDER BY transaction_date 
        ROWS BETWEEN 7 PRECEDING AND CURRENT ROW
    ) AS rolling_7d_spend_velocity
FROM transactions
