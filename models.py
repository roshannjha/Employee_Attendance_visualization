from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON  # Use JSON type for PostgreSQL

db = SQLAlchemy()

class EmployeeData(db.Model):
    __tablename__ = 'employee_data'
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON)  # JSON field to store preprocessed data

    def __repr__(self):
        return f'<EmployeeData {self.id}>'
