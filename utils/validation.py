from flask import jsonify

def require_fields(payload: dict, fields: list):
    for f in fields:
        if f not in payload or payload[f] in (None, ""):
            return jsonify({"error": f"'{f}' is required"}), 400
    return None

def get_pagination_args(args):
    try:
        page = max(int(args.get("page", 1)), 1)
        size = min(max(int(args.get("size", 20)), 1), 200)
    except Exception:
        page, size = 1, 20
    return page, size
