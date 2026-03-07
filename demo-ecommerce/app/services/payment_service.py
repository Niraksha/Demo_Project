import os
import sqlite3

# Issue 1: Hardcoded AWS Secrets (Security Scan will catch this)
AWS_ACCESS_KEY = "AKIA1234567890EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

class PaymentService:
    def __init__(self):
        self.db_path = "payments.db"

    def process_payment(self, user_id, amount):
        print(f"Processing payment of ${amount} for user {user_id}")
        
        # Issue 2: SQL Injection (Security Scan will catch this)
        # Using string formatting instead of parameterized queries
        query = f"SELECT * FROM transactions WHERE user_id = '{user_id}'"
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(query) # Dangerous!
        return True

    # Issue 3: Dead Code (Never called in the PR or project)
    def legacy_refund_method(self, transaction_id):
        """This is an unused function that ARIA will flag as Dead Code."""
        print(f"Refund attempted for {transaction_id}")
        return False

# End of payment_service.py
