-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT *
FROM crime_scene_reports
WHERE year = 2025
AND month = 7
AND day = 28
AND street = 'Humphrey Street';

-- Read witness interviews from that day
SELECT *
FROM interviews
WHERE year = 2025
AND month = 7
AND day = 28;

-- Find cars that left the bakery parking lot shortly after the theft
SELECT *
FROM bakery_security_logs
WHERE year = 2025
AND month = 7
AND day = 28
AND hour = 10
AND minute BETWEEN 15 AND 25;

-- Find withdrawals from the Leggett Street ATM
SELECT *
FROM atm_transactions
WHERE year = 2025
AND month = 7
AND day = 28
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';

-- Find short phone calls made that day
SELECT *
FROM phone_calls
WHERE year = 2025
AND month = 7
AND day = 28
AND duration < 60;

-- Find the earliest flight on July 29
SELECT *
FROM flights
WHERE year = 2025
AND month = 7
AND day = 29
ORDER BY hour, minute
LIMIT 1;

-- List passengers on that flight
SELECT *
FROM passengers
WHERE flight_id = 36;

-- Identify the passengers on that flight
SELECT name, passport_number, license_plate, phone_number
FROM people
WHERE passport_number IN
(
7214083635,
1695452385,
5773159633,
1540955065,
8294398571,
1988161715,
9878712108,
8496433585
);

-- Find people who withdrew money from the Leggett Street ATM
SELECT people.name
FROM people
JOIN bank_accounts
ON people.id = bank_accounts.person_id
JOIN atm_transactions
ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.year = 2025
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_transactions.atm_location = 'Leggett Street'
AND atm_transactions.transaction_type = 'withdraw';

-- Find Bruce's phone call to identify the accomplice
SELECT p.name
FROM phone_calls pc
JOIN people p
ON pc.receiver = p.phone_number
WHERE pc.caller = (
    SELECT phone_number
    FROM people
    WHERE name = 'Bruce'
)
AND pc.year = 2025
AND pc.month = 7
AND pc.day = 28
AND pc.duration < 60;

-- Find the destination city of Flight 36
SELECT city
FROM airports
WHERE id = (
    SELECT destination_airport_id
    FROM flights
    WHERE id = 36
);


