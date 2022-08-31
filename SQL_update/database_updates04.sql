
ALTER TABLE eventos ADD telegram_sent TIMESTAMP NULL DEFAULT NULL;
ALTER TABLE eventos add telegram_result varchar(20) DEFAULT NULL;