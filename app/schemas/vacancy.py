from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class VacancyBase(BaseModel):
    title: str
    timetable_mode_name: str
    tag_name: str
    city_name: Optional[str] = None
    published_at: datetime
    is_remote_available: bool
    is_hot: bool
    # FIX: Убрал external_id из базы, чтобы он не наследовался в Update


class VacancyCreate(VacancyBase):
    external_id: int # FIX: Добавил external_id, так как при создании он нужен


class VacancyUpdate(VacancyBase):
    # FIX: Убрал external_id, поле защищено от изменений
    pass


class VacancyRead(VacancyBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    external_id: Optional[int] = None # Показываем в ответах API
    created_at: datetime
