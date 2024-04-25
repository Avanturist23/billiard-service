from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import BilliardOut, BilliardIn, billiardUpdate
from app.api import db_manager
from app.api.service import is_label_present

billiard = APIRouter()

@billiard.post('/', response_model=BilliardIn, status_code=201)
async def create_billiard(payload: BilliardIn):
    for label_id in payload.labels_id:
        if not is_label_present(label_id):
            raise HTTPException(status_code=404, detail=f"Label with given id:{label_id} not found")

    billiard_id = await db_manager.add_billiard(payload)
    response = {
        'id': billiard_id,
        **payload.dict()
    }

    return response

@billiard.get('/', response_model=List[BilliardOut])
async def get_billiards():
    return await db_manager.get_all_billiards()

@billiard.get('/{id}/', response_model=BilliardOut)
async def get_billiard(id: int):
    billiard = await db_manager.get_billiard(id)
    if not billiard:
        raise HTTPException(status_code=404, detail="billiard not found")
    return billiard

@billiard.put('/{id}/', response_model=BilliardOut)
async def update_billiard(id: int, payload: billiardUpdate):
    billiard = await db_manager.get_billiard(id)
    if not billiard:
        raise HTTPException(status_code=404, detail="Label not found")

    update_data = payload.dict(exclude_unset=True)

    if 'labels_id' in update_data:
        for label_id in payload.labels_id:
            if not is_label_present(label_id):
                raise HTTPException(status_code=404, detail=f"Label with given id:{label_id} not found")

    billiard_in_db = BilliardIn(**billiard)

    updated_billiard = billiard_in_db.copy(update=update_data)

    return await db_manager.update_billiard(id, updated_billiard)

@billiard.delete('/{id}/', response_model=None)
async def delete_billiard(id: int):
    billiard = await db_manager.get_billiard(id)
    if not billiard:
        raise HTTPException(status_code=404, detail="billiard not found")
    return await db_manager.delete_billiard(id)