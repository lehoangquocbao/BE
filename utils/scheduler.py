from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from models import db
from models.class_appointment import Appointment  # đổi tên nếu class khác
from flask import current_app

_scheduler = None

def _remind_tomorrow():
    # Ví dụ: tìm lịch hẹn ngày mai và "gửi" nhắc nhở (ở đây log ra)
    try:
        tomorrow = (datetime.utcnow() + timedelta(days=1)).date()
        q = db.session.query(Appointment).filter(
            db.func.date(Appointment.date) == tomorrow
        )
        count = q.count()
        current_app.logger.info(f"[Scheduler] Nhắc nhở {count} lịch hẹn ngày {tomorrow}")
        # TODO: tích hợp email/SMS/Push tại đây
    except Exception as e:
        current_app.logger.exception(f"[Scheduler] Error: {e}")

def start_scheduler(app):
    global _scheduler
    if _scheduler:
        return _scheduler

    scheduler = BackgroundScheduler(timezone="UTC")
    # Chạy mỗi ngày 01:00 UTC
    scheduler.add_job(_remind_tomorrow, "cron", hour=1, minute=0, id="remind_tomorrow")
    scheduler.start()
    app.logger.info("Scheduler started")
    _scheduler = scheduler
    return sche
