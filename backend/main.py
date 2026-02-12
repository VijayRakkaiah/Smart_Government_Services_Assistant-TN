from fastapi import FastAPI
from pydantic import BaseModel

from backend.agents.planner_agent import plan_user_request
from backend.agents.scheme_agent import get_scheme_info
from backend.agents.form_agent import generate_application_form
from backend.agents.language_agent import detect_language

app = FastAPI()

class UserRequest(BaseModel):
    query: str

@app.post("/assist")
def assist(req: UserRequest):

    language = detect_language(req.query)

    plan = plan_user_request(req.query)

    scheme_data = get_scheme_info(req.query)

    form = generate_application_form(req.query, scheme_data)

    return {
        "language": language,
        "plan": plan,
        "scheme": scheme_data,
        "application_draft": form
    }
