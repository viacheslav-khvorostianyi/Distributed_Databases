-- Initialize user_counter table
DROP TABLE IF EXISTS user_counter;

CREATE TABLE user_counter (
    user_id INTEGER PRIMARY KEY,
    counter INTEGER NOT NULL DEFAULT 0,
    version INTEGER NOT NULL DEFAULT 0
);

-- Insert initial record for user_id = 1
INSERT INTO user_counter (user_id, counter, version)
VALUES (1, 0, 0);

-- Verify
SELECT * FROM user_counter;

