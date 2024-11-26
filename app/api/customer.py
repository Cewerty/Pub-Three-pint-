from fastapi import APIRouter, HTTPException


router = APIRouter(prefix='/clients', tags=['Работа с клиентами'])

@router.post('/something')
async def something_users():
    return {'something': 'something'}