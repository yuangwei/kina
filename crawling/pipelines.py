import sqlite3

class AnalysisPipeline:
    def __init__(self):
        self.conn = sqlite3.connect("analysis.db")
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                opportunity TEXT,
                description TEXT,
                evidence TEXT
            )
        """)

    def process_item(self, item, spider):
        for opportunity in item["opportunities"]:
            self.conn.execute(
                "INSERT INTO analysis (opportunity, description, evidence) VALUES (?, ?, ?)",
                (
                    opportunity["opportunity"],
                    opportunity["description"],
                    "\n".join(opportunity["evidence"]),
                ),
            )
        self.conn.commit()
        return item