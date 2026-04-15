from fastapi import FastAPI, HTTPException
from app.models.schemas import ResearchRequest, ResearchPlanResponse
from app.services.planner import generate_research_plan
from app.services.storage import create_report, get_all_reports, get_report_by_id

app = FastAPI(title="Market Research Assistant API")


@app.get("/")
def root():
    return {"message": "Market Research Assistant API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/plan", response_model=ResearchPlanResponse)
def plan_research(request: ResearchRequest):
    plan = generate_research_plan(request.topic)
    saved_report = create_report(plan)
    return saved_report


@app.get("/reports")
def list_reports():
    return get_all_reports()


@app.get("/reports/{report_id}")
def fetch_report(report_id: str):
    report = get_report_by_id(report_id)

    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")

    return report