from sqlalchemy import func

from app.database.connection import SessionLocal
from app.database.models import APIUsage


class Repository:

    def get_total_usage(self):

        with SessionLocal() as db:

            result = db.query(
                func.coalesce(
                    func.sum(APIUsage.input_tokens), 0
                ),
                func.coalesce(
                    func.sum(APIUsage.output_tokens), 0
                ),
                func.coalesce(
                    func.sum(APIUsage.total_tokens), 0
                ),
                func.sum(APIUsage.estimated_cost_usd)
            ).one()

            return {
                "input_tokens": result[0],
                "output_tokens": result[1],
                "total_tokens": result[2],
                "estimated_cost_usd": result[3]
            }