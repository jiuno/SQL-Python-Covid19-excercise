-- Bruno Fernando Alliani

-- Excercise 1.1

CREATE VIEW  mrr_per_account as (SELECT accounts.id as account ,
 SUM(revenue_mrr.amount_inc_tax) as mrr
 from accounts INNER JOIN revenue_mrr ON accounts.id = revenue_mrr.account_id
GROUP BY accounts.id
);

CREATE VIEW  mrr_usage_per_account as (SELECT accounts.id as account ,
  SUM(revenue_usage.amount_inc_tax) as usage
 from accounts INNER JOIN revenue_usage ON  accounts.id = revenue_usage.account_id
GROUP BY accounts.id
);

CREATE VIEW  mrr_orders_success_per_account as (SELECT accounts.id as account ,
 SUM(orders.amount_inc_tax) as paid
 from accounts INNER JOIN orders ON accounts.id = orders.account_id and orders.payment_status = 'success'
GROUP BY accounts.id
);

SELECT mrr_usage_per_account.account,mrr,usage,paid  from mrr_per_account INNER JOIN mrr_usage_per_account ON mrr_per_account.account = mrr_usage_per_account.account
inner JOIN  mrr_orders_success_per_account ON mrr_per_account.account = mrr_orders_success_per_account.account ;


-- Excercise 1.2
select EXTRACT(MONTH FROM revenue_mrr.created_at) as mes, accounts.plan ,'mrr' as revenue_type ,  SUM(revenue_mrr.ammount_inc_tax) as amount  from accounts
inner join revenue_mrr on revenue_mrr.account_id = accounts.id
GROUP by  EXTRACT(MONTH FROM revenue_mrr.created_at) , accounts.plan

UNION

select EXTRACT(MONTH FROM revenue_usage.created_at) as mes, accounts.plan ,'usage' as revenue_type ,  SUM(revenue_usage.ammount_inc_tax) as amount  from accounts
inner join revenue_usage on revenue_usage.account_id = accounts.id
GROUP by  EXTRACT(MONTH FROM revenue_usage.created_at) , accounts.plan;


-- Excercise 1.3
select EXTRACT(MONTH FROM revenue_mrr.created_at) as month, accounts.id as account ,  SUM(revenue_mrr.ammount_inc_tax) as amount  from accounts
inner join revenue_mrr on revenue_mrr.account_id = accounts.id
GROUP by  EXTRACT(MONTH FROM revenue_mrr.created_at),accounts.id
HAVING  SUM(revenue_mrr.ammount_inc_tax) > 0;

