from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import logging

logger = logging.getLogger(__name__)

class SecurityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Example role-based access control logic
        user_role = request.headers.get("X-User-Role")
        if not user_role:
            logger.warning("Access denied: No role provided")
            return Response("Access denied: No role provided", status_code=403)

        if not self.is_authorized(user_role, request.url.path):
            logger.warning(f"Access denied: Role {user_role} not authorized for {request.url.path}")
            return Response("Access denied: Unauthorized role", status_code=403)

        return await call_next(request)

    def is_authorized(self, role: str, path: str) -> bool:
        # Define role-based access control rules
        role_permissions = {
            "admin": ["/customers", "/projects", "/linking"],
            "user": ["/customers", "/projects"],
            "guest": ["/customers"],
        }

        for allowed_path in role_permissions.get(role, []):
            if path.startswith(allowed_path):
                return True
        return False
