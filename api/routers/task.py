from typing import List

from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter()


@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のTODOタスク")]


@router.get("/tasks/projects/{project_id}/sites/{site_id}/scans/{scan_id}/lod/{lod}/pcd/{suffix}/signeds3download")
async def get_tasks(
    project_id: str,
    site_id: str,
    scan_id: str,
    lod: str,
    suffix: str,
) -> None:
    return {"project_id": project_id, "site_id": site_id, "scan_id": scan_id, "load": lod, "suffix": suffix}


@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())


@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass


def test():
    print("何やかんや")
    pass
