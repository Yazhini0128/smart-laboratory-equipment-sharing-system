# Database Design
The project uses SQLite. Suggested logical entities:
- **Students:** authorised student identifiers and RFID UID mappings.
- **Equipment:** equipment ID, description, and current availability.
- **Waiting Queue:** queued requests in FCFS order.
- **Transactions/Audit Logs:** access attempts, allocations, returns, and denied requests.

Relationships: a student can make many requests; equipment has many historical transactions; queue records reference a student and requested equipment. Confirm table and column names against `database/schema.sql` before calling this the exact implemented schema. Do not publish real RFID UIDs, credentials, or encryption keys.
